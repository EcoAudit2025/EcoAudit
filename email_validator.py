"""
Email validation module for EcoAudit
Validates email addresses by checking domain existence and format
"""
import re
import socket
import smtplib
from typing import Tuple, Optional

def validate_email_format(email: str) -> bool:
    """Basic email format validation"""
    if not email:
        return False
    
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def check_domain_exists(domain: str) -> bool:
    """Check if domain has MX record (mail server)"""
    try:
        # Check for MX record
        import dns.resolver
        mx_records = dns.resolver.resolve(domain, 'MX')
        return len(mx_records) > 0
    except:
        # Fallback: try basic DNS lookup
        try:
            socket.gethostbyname(domain)
            return True
        except socket.gaierror:
            return False

def validate_email_existence(email: str) -> Tuple[bool, str]:
    """
    Validate if email address exists in reality
    Returns: (is_valid, message)
    """
    if not email:
        return False, "Email address is required"
    
    # Basic format check
    if not validate_email_format(email):
        return False, "Invalid email format"
    
    # Extract domain
    try:
        domain = email.split('@')[1].lower()
    except IndexError:
        return False, "Invalid email format"
    
    # Check common domains first (faster)
    common_domains = {
        'gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 
        'aol.com', 'icloud.com', 'protonmail.com', 'mail.com',
        'zoho.com', 'yandex.com', 'live.com', 'msn.com'
    }
    
    if domain in common_domains:
        return True, "Valid email domain"
    
    # For other domains, check if domain exists
    if check_domain_exists(domain):
        return True, "Valid email domain"
    else:
        return False, "Invalid email - domain doesn't exist"

def advanced_email_validation(email: str) -> Tuple[bool, str]:
    """
    Advanced email validation with SMTP verification
    More thorough but slower validation
    """
    basic_valid, basic_msg = validate_email_existence(email)
    if not basic_valid:
        return basic_valid, basic_msg
    
    domain = email.split('@')[1].lower()
    
    # Skip SMTP check for common providers (they block it anyway)
    common_domains = {
        'gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 
        'aol.com', 'icloud.com', 'protonmail.com'
    }
    
    if domain in common_domains:
        return True, "Valid email from trusted provider"
    
    try:
        # Get MX record
        import dns.resolver
        mx_records = dns.resolver.resolve(domain, 'MX')
        mx_record = str(mx_records[0].exchange)
        
        # Connect to mail server
        server = smtplib.SMTP(timeout=10)
        server.connect(mx_record, 25)
        server.helo()
        server.mail('test@example.com')
        code, message = server.rcpt(email)
        server.quit()
        
        # Check response code
        if code == 250:
            return True, "Email verified with mail server"
        else:
            return False, "Email rejected by mail server"
            
    except Exception as e:
        # If SMTP fails, fall back to domain check
        return True, "Email domain exists (SMTP check unavailable)"

def check_email_in_database(email: str) -> bool:
    """Check if email already exists in database"""
    try:
        import database as db
        users = db.get_all_users()
        for user in users:
            if hasattr(user, 'email') and user.email and user.email.lower() == email.lower():
                return True
        return False
    except Exception:
        return False

def validate_email_for_registration(email: str) -> Tuple[bool, str]:
    """
    Complete email validation for registration
    Returns: (is_valid, message)
    """
    # Check if already in database
    if check_email_in_database(email):
        return False, "Email already taken, try something else"
    
    # Check if email exists in reality
    exists, message = validate_email_existence(email)
    if not exists:
        return False, "Invalid email, email doesn't exist"
    
    return True, "Email is valid and available"