"""
Simple AI Models for EcoAudit
Lightweight AI functionality for environmental analysis
"""
import random
from typing import Dict, List, Tuple, Optional

class EcoAI:
    """Simple AI model for environmental analysis"""
    
    def __init__(self):
        self.efficiency_thresholds = {
            'water': {'low': 50, 'moderate': 100, 'high': 150},
            'electricity': {'low': 300, 'moderate': 600, 'high': 900},
            'gas': {'low': 50, 'moderate': 100, 'high': 150}
        }
        
    def analyze_usage(self, water_gallons: float, electricity_kwh: float, gas_cubic_m: float) -> Dict:
        """Analyze utility usage and provide insights"""
        analysis = {
            'water_status': self._get_usage_status('water', water_gallons),
            'electricity_status': self._get_usage_status('electricity', electricity_kwh),
            'gas_status': self._get_usage_status('gas', gas_cubic_m),
            'overall_efficiency': 0.0,
            'recommendations': []
        }
        
        # Calculate overall efficiency score
        efficiency_scores = []
        for utility, value in [('water', water_gallons), ('electricity', electricity_kwh), ('gas', gas_cubic_m)]:
            if value <= self.efficiency_thresholds[utility]['low']:
                efficiency_scores.append(90)
            elif value <= self.efficiency_thresholds[utility]['moderate']:
                efficiency_scores.append(70)
            elif value <= self.efficiency_thresholds[utility]['high']:
                efficiency_scores.append(50)
            else:
                efficiency_scores.append(30)
        
        analysis['overall_efficiency'] = sum(efficiency_scores) / len(efficiency_scores)
        
        # Generate recommendations
        analysis['recommendations'] = self._generate_recommendations(water_gallons, electricity_kwh, gas_cubic_m)
        
        return analysis
    
    def _get_usage_status(self, utility: str, value: float) -> str:
        """Get usage status for a utility"""
        thresholds = self.efficiency_thresholds[utility]
        if value <= thresholds['low']:
            return 'excellent'
        elif value <= thresholds['moderate']:
            return 'good'
        elif value <= thresholds['high']:
            return 'moderate'
        else:
            return 'high'
    
    def _generate_recommendations(self, water: float, electricity: float, gas: float) -> List[str]:
        """Generate personalized recommendations"""
        recommendations = []
        
        if water > self.efficiency_thresholds['water']['moderate']:
            recommendations.append("Consider installing low-flow fixtures to reduce water consumption")
            recommendations.append("Fix any leaks promptly to prevent water waste")
        
        if electricity > self.efficiency_thresholds['electricity']['moderate']:
            recommendations.append("Switch to LED bulbs for energy-efficient lighting")
            recommendations.append("Unplug devices when not in use to reduce phantom loads")
        
        if gas > self.efficiency_thresholds['gas']['moderate']:
            recommendations.append("Improve home insulation to reduce heating/cooling needs")
            recommendations.append("Consider a programmable thermostat for better temperature control")
        
        if not recommendations:
            recommendations.append("Great job! Your usage is efficient across all utilities")
            recommendations.append("Continue monitoring your consumption to maintain these levels")
        
        return recommendations
    
    def assess_usage_with_context(self, water_gallons: float, electricity_kwh: float, gas_cubic_m: float, user_context=None, data_for_analysis=None):
        """Enhanced usage assessment with user context"""
        # Get basic analysis
        analysis = self.analyze_usage(water_gallons, electricity_kwh, gas_cubic_m)
        
        # Return status tuple for compatibility
        return (
            analysis['water_status'],
            analysis['electricity_status'], 
            analysis['gas_status']
        )
    
    def generate_recommendations(self, water: float, electricity: float, gas: float):
        """Generate basic recommendations"""
        return self._generate_recommendations(water, electricity, gas)
    
    def generate_contextual_recommendations(self, water: float, electricity: float, gas: float, user=None):
        """Generate contextual recommendations with user data"""
        recommendations = self._generate_recommendations(water, electricity, gas)
        
        if user and hasattr(user, 'housing_type'):
            if 'apartment' in user.housing_type.lower():
                recommendations.append("Consider energy-efficient appliances suitable for apartment living")
            elif 'house' in user.housing_type.lower():
                recommendations.append("Explore whole-house energy solutions like better insulation")
        
        return recommendations
    
    def analyze_usage_patterns(self, data_for_analysis):
        """Analyze usage patterns from historical data"""
        if not data_for_analysis:
            return {'efficiency_score': 50, 'predictions': None}
        
        # Calculate average efficiency from historical data
        total_efficiency = 0
        count = 0
        
        for record in data_for_analysis:
            water = record.get('water_gallons', 0)
            electricity = record.get('electricity_kwh', 0) 
            gas = record.get('gas_cubic_m', 0)
            
            # Calculate efficiency for this record
            water_eff = 100 if water <= 50 else max(0, 100 - (water - 50) * 0.5)
            elec_eff = 100 if electricity <= 300 else max(0, 100 - (electricity - 300) * 0.1)
            gas_eff = 100 if gas <= 50 else max(0, 100 - (gas - 50) * 1.0)
            
            total_efficiency += (water_eff + elec_eff + gas_eff) / 3
            count += 1
        
        avg_efficiency = total_efficiency / count if count > 0 else 50
        
        return {
            'efficiency_score': avg_efficiency,
            'predictions': f"Based on {count} historical records, your average efficiency is {avg_efficiency:.1f}%"
        }
    
    @property
    def is_trained(self):
        """Check if AI model is trained"""
        return True  # Simple models are always ready

class MaterialAI:
    """Enhanced AI model for comprehensive material analysis"""
    
    def __init__(self):
        self.material_database = {
            # Plastics - Comprehensive coverage
            'plastic': {
                'reuse_tips': [
                    "Clean containers can be used for food storage and organization",
                    "Plastic bottles make excellent planters for herbs and small plants",
                    "Use plastic containers for organizing small items like screws, buttons, or craft supplies",
                    "Create bird feeders, watering cans, or piggy banks from plastic bottles",
                    "Cut plastic containers to make funnels, scoops, or storage compartments"
                ],
                'recycle_tips': [
                    "Check recycling number (1-7) - types 1 (PET), 2 (HDPE), and 5 (PP) are commonly recycled",
                    "Remove caps and labels before recycling unless your facility accepts them",
                    "Rinse containers thoroughly to remove food residue",
                    "Never put plastic bags in curbside recycling - take to store drop-off locations",
                    "Separate different plastic types if required by your local facility"
                ],
                'sustainability_score': 65,
                'category': 'synthetic polymer',
                'environmental_impact': 7.2,
                'recyclability': 6.8
            },
            'plastic bottle': {
                'reuse_tips': [
                    "Create self-watering planters by cutting and inverting the top",
                    "Make bird feeders by cutting holes and adding perches",
                    "Use as storage containers for garage or workshop items",
                    "Create piggy banks or coin collectors for children",
                    "Cut into funnels for various household uses"
                ],
                'recycle_tips': [
                    "Most plastic bottles (PET #1, HDPE #2) are highly recyclable",
                    "Remove caps unless your recycling facility accepts them attached",
                    "Rinse thoroughly but don't need to be spotless",
                    "Crush bottles to save space but don't flatten completely",
                    "Check local guidelines for specific requirements"
                ],
                'sustainability_score': 70,
                'category': 'recyclable plastic',
                'environmental_impact': 6.5,
                'recyclability': 8.2
            },
            'plastic bag': {
                'reuse_tips': [
                    "Use as trash liners for small bins",
                    "Store and organize items in closets or drawers",
                    "Protect items during moving or storage",
                    "Use for pet waste disposal",
                    "Create waterproof storage for camping or travel"
                ],
                'recycle_tips': [
                    "NEVER put in curbside recycling bins - they jam machinery",
                    "Take to grocery store or retailer drop-off locations",
                    "Must be clean and dry for recycling",
                    "Include other plastic films like bread bags, cereal liners",
                    "Look for 'Store Drop-Off' recycling symbol"
                ],
                'sustainability_score': 45,
                'category': 'plastic film',
                'environmental_impact': 8.1,
                'recyclability': 4.2
            },
            
            # Glass - Enhanced details
            'glass': {
                'reuse_tips': [
                    "Glass jars are perfect for food storage - they're airtight and non-toxic",
                    "Use glass containers for DIY candles or luminaries",
                    "Glass bottles can become decorative vases or water containers",
                    "Create spice storage systems with small glass jars",
                    "Use for craft storage - buttons, beads, small hardware"
                ],
                'recycle_tips': [
                    "Glass is 100% recyclable and can be recycled infinitely without quality loss",
                    "Separate by color (clear, brown, green) if required in your area",
                    "Remove metal lids and plastic labels - these go in separate recycling",
                    "Rinse but don't need to be perfectly clean",
                    "Broken glass should be wrapped safely and may need special handling"
                ],
                'sustainability_score': 92,
                'category': 'inorganic recyclable',
                'environmental_impact': 3.1,
                'recyclability': 9.8
            },
            
            # Metals - Comprehensive coverage
            'metal': {
                'reuse_tips': [
                    "Metal containers are excellent for tool storage and organization",
                    "Aluminum cans can become planters with proper drainage holes",
                    "Use tin cans for DIY craft projects and decorative items",
                    "Metal items can be repurposed for garden art or functional uses",
                    "Small metal pieces work well for weights or anchors"
                ],
                'recycle_tips': [
                    "Metals are among the most valuable materials for recycling",
                    "Clean containers but they don't need to be spotless",
                    "Separate different types of metals if required locally",
                    "Aluminum cans are especially valuable - can be recycled infinitely",
                    "Remove non-metal parts like plastic labels or rubber gaskets"
                ],
                'sustainability_score': 94,
                'category': 'recyclable metal',
                'environmental_impact': 2.8,
                'recyclability': 9.5
            },
            'aluminum can': {
                'reuse_tips': [
                    "Create candle holders or luminaries with decorative holes",
                    "Make pencil cups or desk organizers",
                    "Use for small plant pots with drainage holes",
                    "Create wind chimes or garden decorations",
                    "Use as measuring cups for garden fertilizer or pet food"
                ],
                'recycle_tips': [
                    "Aluminum cans are extremely valuable for recycling",
                    "Can be recycled infinitely without losing quality",
                    "Rinse briefly but don't need to be perfectly clean",
                    "Crushing saves space but isn't required",
                    "Recycling one can saves enough energy to power a TV for 3 hours"
                ],
                'sustainability_score': 96,
                'category': 'highly recyclable metal',
                'environmental_impact': 2.2,
                'recyclability': 9.9
            },
            
            # Electronics - Detailed coverage
            'battery': {
                'reuse_tips': [
                    "Rechargeable batteries can be recharged hundreds of times",
                    "Test old batteries - some may still have partial charge for low-power devices",
                    "Single-use batteries cannot be safely reused",
                    "Keep battery testers to check remaining power",
                    "Store properly to extend lifespan of rechargeable batteries"
                ],
                'recycle_tips': [
                    "NEVER throw batteries in regular trash - they contain toxic materials",
                    "Take to battery recycling centers, electronics stores, or hazardous waste facilities",
                    "Many retailers (Best Buy, Home Depot) have free battery recycling",
                    "Car batteries can be returned to auto parts stores",
                    "Lithium batteries from phones/laptops need special e-waste recycling"
                ],
                'sustainability_score': 35,
                'category': 'hazardous e-waste',
                'environmental_impact': 8.7,
                'recyclability': 7.8
            },
            'phone': {
                'reuse_tips': [
                    "Use old phones as dedicated music players or alarm clocks",
                    "Repurpose as security cameras with appropriate apps",
                    "Use as GPS devices for cars or outdoor activities",
                    "Donate working phones to domestic violence shelters",
                    "Keep as emergency backup phones"
                ],
                'recycle_tips': [
                    "Manufacturer take-back programs often offer trade-in value",
                    "Certified e-waste recyclers can recover valuable materials",
                    "Remove and securely erase all personal data first",
                    "Many carriers and retailers offer recycling programs",
                    "Contains valuable metals like gold, silver, and rare earth elements"
                ],
                'sustainability_score': 68,
                'category': 'valuable e-waste',
                'environmental_impact': 6.8,
                'recyclability': 8.5
            },
            
            # Paper products
            'paper': {
                'reuse_tips': [
                    "Use both sides of paper before disposing",
                    "Shred for packaging material or compost (if ink is soy-based)",
                    "Create art projects with old newspapers and magazines",
                    "Use for gift wrapping or craft projects",
                    "Make paper mache or origami projects"
                ],
                'recycle_tips': [
                    "Keep paper dry and clean for optimal recycling",
                    "Remove staples, plastic windows, and tape from envelopes",
                    "Separate cardboard from regular paper if required",
                    "Avoid recycling paper with food contamination",
                    "Shredded paper may need special handling - check locally"
                ],
                'sustainability_score': 85,
                'category': 'biodegradable recyclable',
                'environmental_impact': 4.2,
                'recyclability': 8.8
            },
            
            # Textiles
            'clothes': {
                'reuse_tips': [
                    "Donate wearable clothes to charity organizations",
                    "Repurpose old t-shirts as cleaning rags or dust cloths",
                    "Use denim for patches or craft projects",
                    "Create quilts or blankets from fabric scraps",
                    "Use as protective covering for furniture during painting"
                ],
                'recycle_tips': [
                    "Textile recycling programs are available in many areas",
                    "Some retailers accept old clothes for recycling",
                    "Separate natural fibers from synthetic blends if possible",
                    "Even worn-out clothes can be recycled into insulation or rags",
                    "Check for local textile recycling drop-off locations"
                ],
                'sustainability_score': 72,
                'category': 'textile waste',
                'environmental_impact': 5.8,
                'recyclability': 6.5
            },
            
            # Rubber products
            'tire': {
                'reuse_tips': [
                    "Create garden planters - excellent drainage and durability",
                    "Make outdoor furniture like ottomans or tables",
                    "Use for playground equipment or exercise apparatus",
                    "Create swings for children or exercise equipment",
                    "Use as protective barriers or bumpers"
                ],
                'recycle_tips': [
                    "Many tire retailers accept old tires for recycling (sometimes for a fee)",
                    "Tires can be recycled into rubber mulch, playground surfaces",
                    "Never burn tires - releases toxic chemicals",
                    "Some municipalities have tire recycling events",
                    "Whole tires can become artificial reefs in marine environments"
                ],
                'sustainability_score': 78,
                'category': 'rubber waste',
                'environmental_impact': 5.2,
                'recyclability': 7.8
            }
        }
    
    def analyze_material(self, material_name: str) -> Dict:
        """Enhanced material analysis with improved matching and comprehensive recommendations"""
        material_lower = material_name.lower().strip()
        
        # Direct exact match first
        if material_lower in self.material_database:
            material_data = self.material_database[material_lower]
            return self._format_analysis_result(material_lower, material_data)
        
        # Enhanced fuzzy matching with priority scoring
        best_match = None
        best_score = 0
        
        for key in self.material_database.keys():
            score = 0
            
            # Exact substring match gets highest priority
            if key in material_lower or material_lower in key:
                score = 100
            # Word-based matching for compound materials
            elif any(word in material_lower for word in key.split()):
                score = 80
            # Partial word matching
            elif any(word[:3] in material_lower for word in key.split() if len(word) > 3):
                score = 60
            
            # Boost score for common material categories
            if any(category in material_lower for category in ['plastic', 'glass', 'metal', 'paper', 'battery']):
                if any(category in key for category in ['plastic', 'glass', 'metal', 'paper', 'battery']):
                    score += 20
            
            if score > best_score:
                best_score = score
                best_match = key
        
        # If we found a good match (score > 50), use it
        if best_match and best_score > 50:
            material_data = self.material_database[best_match]
            return self._format_analysis_result(best_match, material_data)
        
        # Enhanced fallback with category-based suggestions
        category = self._categorize_unknown_material(material_lower)
        return self._generate_fallback_analysis(material_lower, category)
    
    def _format_analysis_result(self, material_type: str, material_data: Dict) -> Dict:
        """Format the analysis result with all required fields"""
        # Convert lists to strings for display
        reuse_tips = material_data['reuse_tips']
        recycle_tips = material_data['recycle_tips']
        
        if isinstance(reuse_tips, list):
            reuse_tips = "\n\n".join([f"• {tip}" for tip in reuse_tips])
        if isinstance(recycle_tips, list):
            recycle_tips = "\n\n".join([f"• {tip}" for tip in recycle_tips])
        
        return {
            'material_type': material_type,
            'category': material_data.get('category', 'general'),
            'sustainability_score': material_data.get('sustainability_score', 50),
            'environmental_impact': material_data.get('environmental_impact', 5.0),
            'recyclability': material_data.get('recyclability', 5.0),
            'reuse_tips': reuse_tips,
            'recycle_tips': recycle_tips
        }
    
    def _categorize_unknown_material(self, material: str) -> str:
        """Categorize unknown materials based on keywords"""
        categories = {
            'electronic': ['electronic', 'digital', 'computer', 'device', 'gadget', 'tech'],
            'plastic': ['polymer', 'synthetic', 'vinyl', 'foam', 'resin'],
            'metal': ['steel', 'iron', 'copper', 'brass', 'alloy', 'metallic'],
            'organic': ['wood', 'natural', 'bio', 'organic', 'plant', 'fiber'],
            'textile': ['fabric', 'cloth', 'textile', 'yarn', 'thread'],
            'ceramic': ['ceramic', 'pottery', 'clay', 'porcelain'],
            'composite': ['composite', 'mixed', 'layered', 'laminated']
        }
        
        for category, keywords in categories.items():
            if any(keyword in material for keyword in keywords):
                return category
        
        return 'unknown'
    
    def _generate_fallback_analysis(self, material: str, category: str) -> Dict:
        """Generate comprehensive fallback analysis for unknown materials"""
        fallback_data = {
            'electronic': {
                'reuse_tips': "• Check if the device can be repaired or refurbished\n• Donate working electronics to schools or community centers\n• Repurpose components for DIY projects or educational purposes\n• Use as spare parts for similar devices",
                'recycle_tips': "• Take to certified e-waste recycling facilities\n• Check manufacturer take-back programs\n• Never dispose in regular trash due to toxic materials\n• Remove batteries and personal data before recycling",
                'sustainability_score': 45,
                'environmental_impact': 7.5,
                'recyclability': 6.8
            },
            'plastic': {
                'reuse_tips': "• Clean thoroughly and repurpose for storage or organization\n• Use for craft projects or DIY solutions\n• Create planters or containers with proper drainage\n• Repurpose based on durability and material properties",
                'recycle_tips': "• Check recycling symbols and numbers (1-7)\n• Clean thoroughly before recycling\n• Follow local recycling guidelines\n• Some plastic types may need special drop-off locations",
                'sustainability_score': 55,
                'environmental_impact': 6.8,
                'recyclability': 5.5
            },
            'metal': {
                'reuse_tips': "• Clean and repurpose for storage or organization\n• Use for craft projects or garden applications\n• Repurpose as weights, tools, or decorative items\n• Consider artistic or functional upcycling projects",
                'recycle_tips': "• Metals are highly valuable for recycling\n• Clean but don't need to be spotless\n• Separate different metal types if possible\n• Take to scrap metal facilities or curbside recycling",
                'sustainability_score': 85,
                'environmental_impact': 3.2,
                'recyclability': 9.0
            },
            'unknown': {
                'reuse_tips': "• Assess if the item can be repaired or refurbished\n• Consider creative repurposing based on material properties\n• Donate if still functional and safe to use\n• Use for appropriate craft or DIY projects",
                'recycle_tips': "• Contact local waste management for guidance\n• Research specialty recycling programs in your area\n• Check with manufacturers for take-back programs\n• Ensure proper disposal if not recyclable",
                'sustainability_score': 50,
                'environmental_impact': 5.0,
                'recyclability': 5.0
            }
        }
        
        data = fallback_data.get(category, fallback_data['unknown'])
        
        return {
            'material_type': material,
            'category': category,
            'sustainability_score': data['sustainability_score'],
            'environmental_impact': data['environmental_impact'],
            'recyclability': data['recyclability'],
            'reuse_tips': data['reuse_tips'],
            'recycle_tips': data['recycle_tips']
        }
    
    def _get_environmental_impact(self, score: int) -> str:
        """Get environmental impact description based on score"""
        if score >= 90:
            return "Excellent - highly sustainable material with minimal environmental impact"
        elif score >= 80:
            return "Good - sustainable material with moderate environmental benefits"
        elif score >= 70:
            return "Fair - some environmental benefits but room for improvement"
        elif score >= 60:
            return "Moderate - limited environmental benefits, consider alternatives"
        else:
            return "Poor - significant environmental impact, seek sustainable alternatives"

# Create instances for import
eco_ai = EcoAI()
material_ai = MaterialAI()