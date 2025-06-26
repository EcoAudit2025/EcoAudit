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
    """Simple AI model for material analysis"""
    
    def __init__(self):
        self.material_database = {
            'plastic': {
                'reuse_tips': [
                    "Clean containers can be used for food storage",
                    "Plastic bottles make great planters for herbs",
                    "Use plastic containers for organizing small items"
                ],
                'recycle_tips': [
                    "Check recycling number - types 1, 2, and 5 are commonly recycled",
                    "Remove caps and labels before recycling",
                    "Rinse containers to remove food residue"
                ],
                'sustainability_score': 60
            },
            'glass': {
                'reuse_tips': [
                    "Glass jars are perfect for food storage",
                    "Use glass containers for DIY candles",
                    "Glass bottles can become decorative vases"
                ],
                'recycle_tips': [
                    "Glass is 100% recyclable and can be recycled indefinitely",
                    "Separate by color if required in your area",
                    "Remove metal lids and plastic labels"
                ],
                'sustainability_score': 95
            },
            'paper': {
                'reuse_tips': [
                    "Use both sides of paper before disposing",
                    "Shred for packaging material or compost",
                    "Create art projects with old newspapers and magazines"
                ],
                'recycle_tips': [
                    "Keep paper dry and clean for recycling",
                    "Remove staples and plastic windows from envelopes",
                    "Separate cardboard from regular paper"
                ],
                'sustainability_score': 85
            },
            'metal': {
                'reuse_tips': [
                    "Aluminum cans can become planters or organizers",
                    "Metal containers are great for tool storage",
                    "Use tin cans for DIY craft projects"
                ],
                'recycle_tips': [
                    "Metals are highly valuable for recycling",
                    "Clean containers but don't need to be spotless",
                    "Separate different types of metals if required"
                ],
                'sustainability_score': 90
            }
        }
    
    def analyze_material(self, material_name: str) -> Dict:
        """Analyze material and provide recommendations"""
        material_lower = material_name.lower()
        
        # Find best match
        best_match = None
        for key in self.material_database.keys():
            if key in material_lower or material_lower in key:
                best_match = key
                break
        
        if not best_match:
            # Provide generic advice
            return {
                'material_type': 'unknown',
                'reuse_tips': [
                    "Consider if the item can be repaired instead of discarded",
                    "Look for creative ways to repurpose the material",
                    "Check with local recycling facilities for disposal options"
                ],
                'recycle_tips': [
                    "Contact your local waste management facility",
                    "Look for specialty recycling programs in your area",
                    "Consider donating if the item is still functional"
                ],
                'sustainability_score': 50,
                'environmental_impact': 'Unknown - please provide more specific material information'
            }
        
        material_data = self.material_database[best_match]
        return {
            'material_type': best_match,
            'reuse_tips': material_data['reuse_tips'],
            'recycle_tips': material_data['recycle_tips'],
            'sustainability_score': material_data['sustainability_score'],
            'environmental_impact': self._get_environmental_impact(material_data['sustainability_score'])
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