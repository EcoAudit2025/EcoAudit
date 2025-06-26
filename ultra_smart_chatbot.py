"""
Ultra Smart Chatbot for EcoAudit
Advanced environmental assistant with comprehensive knowledge and personality
"""
import random
import re
from datetime import datetime
from typing import List, Dict, Optional, Tuple

class UltraSmartChatbot:
    """Ultra intelligent environmental chatbot with personality and deep knowledge"""
    
    def __init__(self):
        self.name = "EcoBot"
        self.personality_traits = {
            'enthusiasm': 0.8,
            'expertise': 0.9,
            'friendliness': 0.9,
            'humor': 0.3
        }
        
        self.conversation_context = {
            'user_profile': {},
            'conversation_history': [],
            'current_topic': None,
            'expertise_level': 'beginner'
        }
        
        self.environmental_knowledge = {
            'carbon_footprint': {
                'facts': [
                    "The average American has a carbon footprint of about 16 tons CO2 per year, while the global average is 4 tons.",
                    "Transportation accounts for about 29% of US greenhouse gas emissions, making it the largest contributor.",
                    "A single tree can absorb 48 pounds of CO2 per year and sequester 1 ton of CO2 by age 40.",
                    "Switching to renewable energy can reduce a household's carbon footprint by 50% or more."
                ],
                'actions': [
                    "Calculate your carbon footprint to identify the biggest reduction opportunities",
                    "Consider carbon offset programs for unavoidable emissions",
                    "Focus on transportation changes - they often have the biggest impact",
                    "Support renewable energy through your utility or community solar programs"
                ]
            },
            'renewable_energy': {
                'facts': [
                    "Solar panel costs have dropped 85% since 2010, making renewable energy more accessible.",
                    "Wind energy is now the cheapest source of electricity in many parts of the world.",
                    "Renewable energy jobs are growing 70% faster than the overall economy.",
                    "Denmark generates over 140% of its electricity needs from wind power during windy periods."
                ],
                'actions': [
                    "Explore solar options for your home through local installers or community programs",
                    "Switch to a renewable energy plan from your utility provider",
                    "Invest in energy storage solutions like home batteries",
                    "Support policies that promote renewable energy development"
                ]
            },
            'sustainable_living': {
                'facts': [
                    "The fashion industry produces 10% of global carbon emissions and is the second-largest consumer of water.",
                    "Food production accounts for 26% of global greenhouse gas emissions.",
                    "Americans throw away about 40% of the food they purchase.",
                    "Plastic pollution affects 700 marine species and enters the food chain through microplastics."
                ],
                'actions': [
                    "Choose quality, durable clothing and consider second-hand options",
                    "Reduce meat consumption and choose locally-sourced foods",
                    "Plan meals to reduce food waste and compost scraps",
                    "Use reusable alternatives to single-use plastics"
                ]
            },
            'water_conservation': {
                'facts': [
                    "It takes 1,800 gallons of water to produce a pound of beef, but only 39 gallons for a pound of vegetables.",
                    "The average American uses 2,000 gallons of water daily when including hidden water in products.",
                    "Agriculture accounts for 70% of global freshwater consumption.",
                    "By 2025, 1.8 billion people will live in areas with absolute water scarcity."
                ],
                'actions': [
                    "Install smart irrigation systems that adjust to weather conditions",
                    "Choose drought-resistant native plants for landscaping",
                    "Fix leaks immediately - a single drip can waste over 3,000 gallons annually",
                    "Consider greywater systems for toilet flushing and irrigation"
                ]
            }
        }
        
        self.response_templates = {
            'enthusiastic': [
                "That's fantastic that you're interested in {topic}! 🌱",
                "I love talking about {topic} - it's one of my favorite environmental topics!",
                "Great question about {topic}! Let me share some exciting information..."
            ],
            'expert': [
                "Based on the latest environmental research on {topic}...",
                "From a scientific perspective on {topic}...",
                "The data shows that when it comes to {topic}..."
            ],
            'encouraging': [
                "You're already making a difference by asking about {topic}!",
                "Every step toward understanding {topic} helps our planet!",
                "Your interest in {topic} shows you care about our environment!"
            ]
        }
    
    def get_ultra_smart_response(self, user_input: str, user_context: Optional[Dict] = None) -> str:
        """Generate ultra-intelligent contextual response"""
        # Update context
        if user_context:
            self.conversation_context['user_profile'].update(user_context)
        
        self.conversation_context['conversation_history'].append({
            'timestamp': datetime.now(),
            'user_input': user_input,
            'user_context': user_context or {}
        })
        
        # Analyze user input sophistication
        self._analyze_user_expertise(user_input)
        
        # Determine response approach
        topic = self._identify_topic(user_input)
        response_style = self._choose_response_style(user_input)
        
        # Generate response
        if topic:
            return self._generate_topic_response(topic, response_style, user_input)
        else:
            return self._generate_general_response(user_input, response_style)
    
    def _analyze_user_expertise(self, user_input: str):
        """Analyze user's expertise level based on language used"""
        technical_terms = [
            'carbon sequestration', 'photovoltaic', 'kilowatt-hour', 'embodied energy',
            'life cycle assessment', 'circular economy', 'biodegradable', 'sustainable yield',
            'renewable portfolio standard', 'carbon offset', 'energy payback time'
        ]
        
        advanced_indicators = [
            'scientific study', 'research shows', 'peer-reviewed', 'methodology',
            'quantitative analysis', 'environmental impact assessment'
        ]
        
        user_lower = user_input.lower()
        
        technical_count = sum(1 for term in technical_terms if term in user_lower)
        advanced_count = sum(1 for indicator in advanced_indicators if indicator in user_lower)
        
        if technical_count >= 2 or advanced_count >= 1:
            self.conversation_context['expertise_level'] = 'expert'
        elif technical_count >= 1 or len(user_input.split()) > 20:
            self.conversation_context['expertise_level'] = 'intermediate'
        else:
            self.conversation_context['expertise_level'] = 'beginner'
    
    def _identify_topic(self, user_input: str) -> Optional[str]:
        """Identify the main environmental topic from user input"""
        user_lower = user_input.lower()
        
        topic_keywords = {
            'carbon_footprint': ['carbon', 'emissions', 'footprint', 'co2', 'greenhouse gas', 'climate change'],
            'renewable_energy': ['solar', 'wind', 'renewable', 'clean energy', 'panels', 'turbine', 'grid'],
            'sustainable_living': ['sustainable', 'eco-friendly', 'green living', 'lifestyle', 'consumption'],
            'water_conservation': ['water', 'conservation', 'drought', 'irrigation', 'aquifer', 'watershed']
        }
        
        for topic, keywords in topic_keywords.items():
            if any(keyword in user_lower for keyword in keywords):
                self.conversation_context['current_topic'] = topic
                return topic
        
        return None
    
    def _choose_response_style(self, user_input: str) -> str:
        """Choose appropriate response style based on input and personality"""
        user_lower = user_input.lower()
        
        if any(word in user_lower for word in ['help', 'advice', 'what should', 'how can']):
            return 'encouraging'
        elif any(word in user_lower for word in ['research', 'study', 'data', 'evidence']):
            return 'expert'
        else:
            return 'enthusiastic'
    
    def _generate_topic_response(self, topic: str, style: str, user_input: str) -> str:
        """Generate detailed response for specific environmental topic"""
        knowledge = self.environmental_knowledge.get(topic, {})
        
        # Choose response template
        template = random.choice(self.response_templates[style])
        intro = template.format(topic=topic.replace('_', ' '))
        
        # Select appropriate content based on expertise level
        fact = random.choice(knowledge.get('facts', ['Environmental facts are fascinating!']))
        action = random.choice(knowledge.get('actions', ['Every small action helps!']))
        
        # Customize response based on expertise level
        if self.conversation_context['expertise_level'] == 'expert':
            response = f"{intro}\n\n📊 Research insight: {fact}\n\n🔬 Advanced recommendation: {action}"
        elif self.conversation_context['expertise_level'] == 'intermediate':
            response = f"{intro}\n\n💡 Key insight: {fact}\n\n✅ Actionable step: {action}"
        else:
            response = f"{intro}\n\n🌍 Did you know? {fact}\n\n🌱 You can help by: {action}"
        
        # Add personalized touch if we have user context
        if self.conversation_context['user_profile']:
            response += self._add_personalized_note()
        
        return response
    
    def _generate_general_response(self, user_input: str, style: str) -> str:
        """Generate general environmental response when no specific topic is identified"""
        general_knowledge = [
            "Environmental protection requires action at individual, community, and policy levels.",
            "The interconnection between human activities and environmental health is becoming increasingly clear.",
            "Sustainable practices today ensure a healthy planet for future generations.",
            "Every environmental challenge is also an opportunity for innovation and positive change."
        ]
        
        practical_actions = [
            "Start with simple changes: reduce energy use, conserve water, and minimize waste.",
            "Support businesses and policies that prioritize environmental sustainability.",
            "Stay informed about environmental issues and share knowledge with others.",
            "Consider the environmental impact of your daily choices and purchases."
        ]
        
        fact = random.choice(general_knowledge)
        action = random.choice(practical_actions)
        
        if style == 'expert':
            return f"From an environmental science perspective: {fact}\n\n🔬 Evidence-based approach: {action}"
        elif style == 'encouraging':
            return f"You're asking great environmental questions! {fact}\n\n🌱 Here's how you can make a difference: {action}"
        else:
            return f"I love discussing environmental topics! {fact}\n\n✨ Exciting opportunity: {action}"
    
    def _add_personalized_note(self) -> str:
        """Add personalized note based on user profile"""
        profile = self.conversation_context['user_profile']
        
        if profile.get('high_energy_usage'):
            return "\n\n🏠 Personal note: Given your energy usage patterns, focusing on efficiency improvements could have significant impact!"
        elif profile.get('water_conscious'):
            return "\n\n💧 Personal note: I see you're already water-conscious - you're on the right track!"
        elif profile.get('waste_reducer'):
            return "\n\n♻️ Personal note: Your waste reduction efforts are making a real difference!"
        else:
            return "\n\n🌟 Keep up your environmental curiosity - learning is the first step to positive change!"
    
    def get_environmental_challenge(self) -> str:
        """Provide a daily environmental challenge"""
        challenges = [
            "🚿 Water Challenge: Take a 5-minute shower today and see how much water you save!",
            "💡 Energy Challenge: Unplug all electronics you're not using for the next hour.",
            "🚶 Transportation Challenge: Walk or bike for one trip you'd normally drive.",
            "🥗 Food Challenge: Eat one plant-based meal today to reduce your carbon footprint.",
            "♻️ Waste Challenge: Find three items to reuse instead of throwing away.",
            "🌱 Learning Challenge: Read about one environmental topic you've never explored.",
            "🛒 Shopping Challenge: Choose one product based on its environmental impact.",
            "🌳 Nature Challenge: Spend 10 minutes outdoors observing local wildlife or plants."
        ]
        
        return f"Here's your daily eco-challenge! {random.choice(challenges)}\n\nEvery small action contributes to a healthier planet! 🌍"
    
    def get_conversation_summary(self) -> str:
        """Provide summary of conversation topics discussed"""
        if not self.conversation_context['conversation_history']:
            return "We haven't chatted yet! I'm here to help with any environmental questions you have."
        
        topics_discussed = set()
        for entry in self.conversation_context['conversation_history']:
            if self.conversation_context.get('current_topic'):
                topics_discussed.add(self.conversation_context['current_topic'])
        
        if topics_discussed:
            topics_list = ', '.join([topic.replace('_', ' ') for topic in topics_discussed])
            return f"Today we've discussed: {topics_list}. I'm excited to continue exploring environmental topics with you!"
        else:
            return "We've had a great general conversation about environmental topics! Feel free to ask about anything specific."

# Create instance for import
ultra_smart_chatbot = UltraSmartChatbot()