"""
Smart chatbot for EcoAudit
Enhanced environmental assistant with contextual responses
"""
import random
import re
from typing import List, Dict, Optional

class SmartChatbot:
    """Enhanced environmental chatbot with smart responses"""
    
    def __init__(self):
        self.conversation_history = []
        self.user_context = {}
        
        self.knowledge_base = {
            'water_facts': [
                "The average American uses about 80-100 gallons of water per day.",
                "A 5-minute shower uses about 10-25 gallons of water.",
                "Fixing a leaky faucet can save over 3,000 gallons per year.",
                "Low-flow toilets can save up to 13,000 gallons annually."
            ],
            'energy_facts': [
                "LED bulbs use 75% less energy than incandescent bulbs.",
                "Heating and cooling account for about 48% of home energy use.",
                "Energy Star appliances can reduce energy consumption by 10-50%.",
                "Phantom loads from electronics can account for 10% of home energy use."
            ],
            'recycling_facts': [
                "Recycling one aluminum can saves enough energy to run a TV for 3 hours.",
                "Glass containers can be recycled endlessly without loss of quality.",
                "Recycling one ton of paper saves 17 trees and 7,000 gallons of water.",
                "It takes 95% less energy to recycle aluminum than to make it from raw materials."
            ],
            'climate_facts': [
                "Transportation accounts for about 29% of US greenhouse gas emissions.",
                "Buildings consume about 40% of total energy in the US.",
                "Forests absorb about 2.6 billion tons of CO2 annually.",
                "Renewable energy now accounts for over 20% of US electricity generation."
            ]
        }
        
        self.responses = {
            'water_conservation': {
                'tips': [
                    "Here are some water conservation tips: Take shorter showers, fix leaks promptly, install low-flow fixtures, and collect rainwater for plants.",
                    "Water-saving strategies include: using a rain barrel, installing drought-resistant plants, running full loads in dishwashers and washing machines.",
                    "Smart water conservation: Use a broom instead of a hose to clean driveways, install smart irrigation systems, and choose native plants for landscaping."
                ],
                'advanced': [
                    "Advanced water conservation involves greywater systems, smart leak detection devices, and xeriscaping with native plants.",
                    "Consider upgrading to high-efficiency appliances, installing permeable paving, and using smart irrigation controllers."
                ]
            },
            'energy_efficiency': {
                'tips': [
                    "Energy efficiency starts with: LED lighting, programmable thermostats, proper insulation, and Energy Star appliances.",
                    "Reduce energy consumption by: sealing air leaks, upgrading windows, using smart power strips, and maintaining HVAC systems.",
                    "Smart energy practices include: using natural lighting, adjusting thermostat settings, and unplugging unused electronics."
                ],
                'advanced': [
                    "Advanced energy efficiency includes: smart home automation, solar panel installation, geothermal systems, and whole-house energy audits.",
                    "Consider upgrading to smart thermostats, installing heat recovery ventilators, and exploring community solar programs."
                ]
            },
            'waste_reduction': {
                'tips': [
                    "Waste reduction hierarchy: Refuse what you don't need, reduce consumption, reuse items creatively, recycle properly, and compost organics.",
                    "Minimize waste by: buying in bulk, choosing products with minimal packaging, repairing instead of replacing, and donating usable items.",
                    "Smart waste management: compost food scraps, recycle electronics properly, use reusable bags and containers, and choose durable products."
                ],
                'advanced': [
                    "Zero waste living involves: eliminating single-use items, making your own products, participating in bulk buying co-ops, and choosing circular economy products.",
                    "Advanced waste reduction includes: vermiculture composting, upcycling projects, and participating in community swap events."
                ]
            }
        }
    
    def get_smart_response(self, user_input: str, user_context: Optional[Dict] = None) -> str:
        """Get intelligent response based on context and history"""
        if user_context:
            self.user_context.update(user_context)
        
        self.conversation_history.append(user_input)
        
        # Analyze user input
        response_category = self._analyze_input(user_input)
        response_level = self._determine_response_level()
        
        # Generate contextual response
        if response_category and response_category in self.responses:
            responses = self.responses[response_category].get(response_level, self.responses[response_category]['tips'])
            base_response = random.choice(responses)
            
            # Add relevant fact
            fact_category = self._get_fact_category(response_category)
            if fact_category:
                fact = random.choice(self.knowledge_base[fact_category])
                return f"{base_response}\n\n💡 Did you know? {fact}"
            
            return base_response
        
        return self._get_general_response(user_input)
    
    def _analyze_input(self, user_input: str) -> Optional[str]:
        """Analyze user input to determine category"""
        user_input_lower = user_input.lower()
        
        water_keywords = ['water', 'shower', 'bath', 'leak', 'faucet', 'irrigation', 'drought']
        energy_keywords = ['energy', 'electricity', 'power', 'electric', 'heat', 'cool', 'lighting', 'appliance']
        waste_keywords = ['waste', 'trash', 'garbage', 'recycle', 'compost', 'reduce', 'reuse']
        
        if any(keyword in user_input_lower for keyword in water_keywords):
            return 'water_conservation'
        elif any(keyword in user_input_lower for keyword in energy_keywords):
            return 'energy_efficiency'
        elif any(keyword in user_input_lower for keyword in waste_keywords):
            return 'waste_reduction'
        
        return None
    
    def _determine_response_level(self) -> str:
        """Determine if user needs basic or advanced information"""
        recent_history = self.conversation_history[-3:] if len(self.conversation_history) >= 3 else self.conversation_history
        
        # Check for advanced keywords in recent conversation
        advanced_keywords = ['advanced', 'technical', 'detailed', 'professional', 'comprehensive', 'system']
        
        for message in recent_history:
            if any(keyword in message.lower() for keyword in advanced_keywords):
                return 'advanced'
        
        return 'tips'
    
    def _get_fact_category(self, response_category: str) -> Optional[str]:
        """Map response category to fact category"""
        mapping = {
            'water_conservation': 'water_facts',
            'energy_efficiency': 'energy_facts',
            'waste_reduction': 'recycling_facts'
        }
        return mapping.get(response_category)
    
    def _get_general_response(self, user_input: str) -> str:
        """Get general environmental response"""
        general_responses = [
            "That's a great environmental question! Here's what I can tell you: Small daily actions like conserving water, saving energy, and reducing waste can make a significant impact on our planet.",
            "Environmental sustainability is about making choices that protect our planet for future generations. Every action counts, from the products we buy to the energy we use.",
            "I'm here to help with environmental questions! Whether it's about conservation, renewable energy, or sustainable living, I can provide practical tips and information.",
            "Protecting our environment involves multiple approaches: reducing resource consumption, choosing sustainable products, and adopting eco-friendly habits in daily life."
        ]
        
        response = random.choice(general_responses)
        
        # Add a random environmental fact
        all_facts = []
        for facts in self.knowledge_base.values():
            all_facts.extend(facts)
        
        fact = random.choice(all_facts)
        return f"{response}\n\n💡 Environmental fact: {fact}"
    
    def get_personalized_tip(self, user_context: Dict) -> str:
        """Get personalized environmental tip based on user context"""
        if 'high_water_usage' in user_context:
            return "Based on your usage patterns, focus on water conservation: shorter showers, fixing leaks, and installing low-flow fixtures."
        elif 'high_energy_usage' in user_context:
            return "Your energy usage suggests focusing on: LED lighting, better insulation, and programmable thermostats."
        elif 'waste_concerns' in user_context:
            return "For waste reduction, try: composting, buying in bulk, and choosing products with minimal packaging."
        else:
            return "Start your environmental journey with simple steps: conserve water, save energy, and reduce waste. Every small action makes a difference!"

# Create instance for import
smart_chatbot = SmartChatbot()