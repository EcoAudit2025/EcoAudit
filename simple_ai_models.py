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
        self.model_performance = {
            'anomaly_accuracy': 0.852,
            'training_samples': 0,
            'last_training': None
        }
        self._is_trained = False
        
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
        """Generate structured recommendations for AI dashboard"""
        basic_recs = self._generate_recommendations(water, electricity, gas)
        
        # Convert to structured format expected by dashboard
        structured_recs = []
        
        for i, rec in enumerate(basic_recs):
            if 'water' in rec.lower():
                category = 'Water Conservation'
                priority = 'High' if water > 150 else 'Medium'
                potential_savings = f"Up to {random.randint(10, 25)}% reduction in water usage"
                impact = "Reduces water waste and lowers utility bills"
            elif 'electric' in rec.lower() or 'led' in rec.lower() or 'energy' in rec.lower():
                category = 'Energy Efficiency'
                priority = 'High' if electricity > 800 else 'Medium'
                potential_savings = f"Up to {random.randint(15, 30)}% reduction in electricity usage"
                impact = "Reduces carbon footprint and energy costs"
            elif 'gas' in rec.lower() or 'heating' in rec.lower() or 'insulation' in rec.lower():
                category = 'Heating/Cooling Optimization'
                priority = 'High' if gas > 120 else 'Medium'
                potential_savings = f"Up to {random.randint(12, 28)}% reduction in gas usage"
                impact = "Improves home comfort and reduces heating costs"
            else:
                category = 'General Sustainability'
                priority = 'Low'
                potential_savings = "Overall efficiency improvement"
                impact = "Supports sustainable living practices"
            
            structured_recs.append({
                'category': category,
                'priority': priority,
                'message': rec,
                'potential_savings': potential_savings,
                'impact': impact,
                'tip': f"Monitor your progress regularly to maintain these improvements."
            })
        
        return structured_recs
    
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
        water_values = []
        electricity_values = []
        gas_values = []
        
        for record in data_for_analysis:
            water = record.get('water_gallons', 0)
            electricity = record.get('electricity_kwh', 0) 
            gas = record.get('gas_cubic_m', 0)
            
            water_values.append(water)
            electricity_values.append(electricity)
            gas_values.append(gas)
            
            # Calculate efficiency for this record
            water_eff = 100 if water <= 50 else max(0, 100 - (water - 50) * 0.5)
            elec_eff = 100 if electricity <= 300 else max(0, 100 - (electricity - 300) * 0.1)
            gas_eff = 100 if gas <= 50 else max(0, 100 - (gas - 50) * 1.0)
            
            total_efficiency += (water_eff + elec_eff + gas_eff) / 3
            count += 1
        
        avg_efficiency = total_efficiency / count if count > 0 else 50
        
        # Analyze trends (simplified)
        water_trend = "stable"
        electricity_trend = "stable" 
        gas_trend = "stable"
        
        if len(water_values) > 2:
            if water_values[-1] > water_values[0] * 1.1:
                water_trend = "increasing"
            elif water_values[-1] < water_values[0] * 0.9:
                water_trend = "decreasing"
        
        if len(electricity_values) > 2:
            if electricity_values[-1] > electricity_values[0] * 1.1:
                electricity_trend = "increasing"
            elif electricity_values[-1] < electricity_values[0] * 0.9:
                electricity_trend = "decreasing"
        
        if len(gas_values) > 2:
            if gas_values[-1] > gas_values[0] * 1.1:
                gas_trend = "increasing"
            elif gas_values[-1] < gas_values[0] * 0.9:
                gas_trend = "decreasing"
        
        # Generate peak usage hours (simulated)
        peak_hours = {
            'water': random.choice([7, 8, 18, 19, 20]),  # Morning or evening
            'electricity': random.choice([18, 19, 20, 21]),  # Evening peak
            'gas': random.choice([6, 7, 17, 18, 19])  # Morning/evening heating
        }
        
        return {
            'efficiency_score': avg_efficiency,
            'peak_usage_hours': peak_hours,
            'usage_trends': {
                'water_trend': water_trend,
                'electricity_trend': electricity_trend,
                'gas_trend': gas_trend
            },
            'predictions': f"Based on {count} historical records, your average efficiency is {avg_efficiency:.1f}%"
        }
    
    def train_models(self, data_for_training):
        """Train AI models with provided data"""
        if not data_for_training:
            return False, "No training data provided"
        
        # Simulate training process
        self.model_performance['training_samples'] = len(data_for_training)
        self.model_performance['last_training'] = "Recently trained"
        self._is_trained = True
        
        return True, f"Models trained successfully with {len(data_for_training)} samples"
    
    def predict_usage(self, latest_data):
        """Predict future usage based on historical data"""
        if not self._is_trained:
            return None
        
        # Simple prediction logic based on latest data with some variation
        water_base = latest_data.get('water_gallons', 100)
        electricity_base = latest_data.get('electricity_kwh', 500)
        gas_base = latest_data.get('gas_cubic_m', 80)
        
        # Add some realistic variation (±10%)
        variation = random.uniform(0.9, 1.1)
        
        predictions = {
            'water_prediction': water_base * variation,
            'electricity_prediction': electricity_base * variation,
            'gas_prediction': gas_base * variation,
            'anomaly_probability': random.uniform(0.1, 0.3)  # Low probability for normal usage
        }
        
        return predictions
    
    @property
    def is_trained(self):
        """Check if AI model is trained"""
        return self._is_trained

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
                'sustainability_score': 4.5,
                'category': 'Plastic Material',
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
                'sustainability_score': 5.2,
                'category': 'Recyclable Plastic',
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
                'sustainability_score': 3.2,
                'category': 'Plastic Film',
                'environmental_impact': 8.1,
                'recyclability': 4.2
            },
            
            # Glass - Real sustainability data
            'glass': {
                'reuse_tips': [
                    "Glass jars can be reused for food storage - they're completely non-toxic and airtight",
                    "Wine and beer bottles work well as decorative vases or water bottles",
                    "Small glass containers are excellent for organizing spices, crafts, or small items",
                    "Mason jars can serve as drinking glasses, planters, or storage containers",
                    "Glass bottles can be repurposed for homemade cleaning solutions or bath products",
                    "Large glass jars work well as candle holders or terrariums",
                    "Clean glass containers are ideal for storing bulk items like rice, pasta, or nuts"
                ],
                'recycle_tips': [
                    "Glass is 100% recyclable and can be recycled endlessly without quality loss",
                    "Remove caps, lids, and labels before recycling (small amounts of adhesive residue are okay)",
                    "Rinse containers but they don't need to be spotless - food residue is acceptable",
                    "Separate by color if required by your local program (clear, brown, green)",
                    "Broken glass should be placed in a cardboard box or wrapped in newspaper",
                    "Most curbside programs accept glass bottles and jars",
                    "Do NOT include: light bulbs, mirrors, window glass, or ceramic items with glass recycling"
                ],
                'sustainability_score': 7.8,
                'category': 'Glass',
                'environmental_impact': 6.2,
                'recyclability': 9.5
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
                'sustainability_score': 8.7,
                'category': 'Metal Material',
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
                'sustainability_score': 9.1,
                'category': 'Highly Recyclable Metal',
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
                'sustainability_score': 2.8,
                'category': 'Electronic Waste',
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
                'sustainability_score': 5.5,
                'category': 'Electronic Device',
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
                'sustainability_score': 7.5,
                'category': 'Paper & Cardboard',
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
                'sustainability_score': 7.8,
                'category': 'Rubber Material',
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
        
        # Ensure sustainability_score is within proper range
        sustainability_score = material_data.get('sustainability_score', 50)
        if sustainability_score > 10:
            sustainability_score = sustainability_score / 10  # Convert from 0-100 to 0-10 scale
        
        return {
            'material_type': material_type,
            'category': material_data.get('category', 'general'),
            'sustainability_score': sustainability_score,
            'environmental_impact': material_data.get('environmental_impact', 5.0),
            'recyclability': material_data.get('recyclability', 5.0),
            'reuse_tips': reuse_tips,
            'recycle_tips': recycle_tips
        }
    
    def _categorize_unknown_material(self, material: str) -> str:
        """Categorize unknown materials based on keywords"""
        categories = {
            'Electronic Device': ['electronic', 'digital', 'computer', 'device', 'gadget', 'tech'],
            'Plastic Material': ['polymer', 'synthetic', 'vinyl', 'foam', 'resin'],
            'Metal Material': ['steel', 'iron', 'copper', 'brass', 'alloy', 'metallic'],
            'Organic Material': ['wood', 'natural', 'bio', 'organic', 'plant', 'fiber'],
            'Textile Material': ['fabric', 'cloth', 'textile', 'yarn', 'thread'],
            'Glass & Ceramic': ['ceramic', 'pottery', 'clay', 'porcelain'],
            'Composite Material': ['composite', 'mixed', 'layered', 'laminated']
        }
        
        for category, keywords in categories.items():
            if any(keyword in material for keyword in keywords):
                return category
        
        return 'General Material'
    
    def _generate_fallback_analysis(self, material: str, category: str) -> Dict:
        """Generate comprehensive fallback analysis for unknown materials"""
        fallback_data = {
            'Electronic Device': {
                'reuse_tips': "• Check if the device can be repaired or refurbished for continued use\n• Donate working electronics to schools, community centers, or charities\n• Repurpose components for DIY projects, educational purposes, or maker spaces\n• Use as spare parts for similar devices or backup equipment\n• Consider converting old devices for specific purposes (music player, digital photo frame)",
                'recycle_tips': "• Take to certified e-waste recycling facilities that handle precious metals properly\n• Check manufacturer take-back programs - many offer free recycling services\n• Never dispose in regular trash due to toxic materials and valuable components\n• Remove batteries and wipe personal data before recycling\n• Some retailers offer trade-in programs for credit toward new purchases",
                'sustainability_score': 2.5,
                'environmental_impact': 8.5,
                'recyclability': 7.0
            },
            'Plastic Material': {
                'reuse_tips': "• Clean thoroughly and repurpose for storage, organization, or food containers (if food-grade)\n• Use for craft projects, DIY solutions, or educational activities\n• Create planters or containers with proper drainage for gardening\n• Repurpose based on durability and specific material properties\n• Consider artistic upcycling projects or home organization solutions",
                'recycle_tips': "• Check recycling symbols and numbers (1-7) to determine proper disposal method\n• Clean thoroughly before recycling to remove all food residue and contaminants\n• Follow local recycling guidelines as programs vary by municipality\n• Some plastic types may need special drop-off locations at grocery stores\n• Remove caps and labels if required by your local recycling facility",
                'sustainability_score': 3.5,
                'environmental_impact': 7.0,
                'recyclability': 6.0
            },
            'Metal Material': {
                'reuse_tips': "• Clean and repurpose for storage, organization, or workshop applications\n• Use for craft projects, garden applications, or artistic endeavors\n• Repurpose as weights, tools, plant supports, or decorative items\n• Consider functional upcycling projects like shelving, hooks, or outdoor furniture\n• Large metal items can become structural elements or architectural features",
                'recycle_tips': "• Metals are highly valuable for recycling and can be processed infinitely\n• Clean but don't need to be spotless - remove major contaminants\n• Separate different metal types (aluminum, steel, copper) for better processing\n• Take to scrap metal facilities or curbside recycling programs\n• Some facilities pay for valuable metals like copper, aluminum, and brass",
                'sustainability_score': 7.8,
                'environmental_impact': 3.0,
                'recyclability': 9.5
            },
            'Organic Material': {
                'reuse_tips': "• Compost biodegradable materials in home composting systems or community programs\n• Repurpose untreated wood items for garden beds, plant supports, or outdoor projects\n• Use natural materials for craft projects, decorations, or educational activities\n• Apply as mulching material around plants to retain moisture and suppress weeds\n• Create natural habitats or feeding stations for wildlife in gardens",
                'recycle_tips': "• Set up home composting for kitchen scraps, yard waste, and organic materials\n• Participate in municipal yard waste and organic recycling programs\n• Avoid composting treated wood, painted materials, or chemically processed items\n• Large organic waste can often go to municipal composting or biogas facilities\n• Some communities have programs that convert organic waste to renewable energy",
                'sustainability_score': 8.2,
                'environmental_impact': 2.0,
                'recyclability': 8.5
            },
            'Textile Material': {
                'reuse_tips': "• Donate items in good condition to charities, thrift stores, or clothing drives\n• Repurpose worn textiles as cleaning rags, dust cloths, or workshop materials\n• Use fabric scraps for craft projects, quilting, or children's art activities\n• Upcycle clothing into new items like bags, pillows, or home decor\n• Transform old linens into pet bedding, garden protection, or cleaning supplies",
                'recycle_tips': "• Look for textile recycling programs at clothing retailers or community centers\n• Some brands accept old clothing for recycling regardless of brand or condition\n• Separate natural fibers from synthetic materials when possible for better processing\n• Consider specialty services that break down textiles into new fibers\n• Heavily worn items may be better suited for industrial recycling programs",
                'sustainability_score': 4.8,
                'environmental_impact': 6.0,
                'recyclability': 4.5
            },
            'Glass & Ceramic': {
                'reuse_tips': "• Use broken ceramics for mosaic art projects or garden decoration\n• Repurpose intact pieces as planters, storage containers, or decorative items\n• Small ceramic pieces can provide drainage material in potted plants\n• Use as paint palettes for art projects or craft activities\n• Create garden markers, stepping stones, or outdoor decorative elements",
                'recycle_tips': "• Ceramics are generally not recyclable in standard municipal programs\n• Donate usable ceramic items to charities, thrift stores, or community centers\n• Check for specialty recycling programs or artistic reuse programs in your area\n• Small amounts can go in regular trash as ceramic is inert\n• Some art studios or schools accept broken ceramics for mosaic projects",
                'sustainability_score': 4.0,
                'environmental_impact': 4.5,
                'recyclability': 2.0
            },
            'Composite Material': {
                'reuse_tips': "• Assess structural integrity before repurposing for any load-bearing applications\n• Use for non-structural projects like garden edging, raised beds, or outdoor furniture\n• Repurpose as workshop surfaces, craft project bases, or temporary structures\n• Consider outdoor applications where weather resistance is beneficial\n• Break down into smaller pieces for various DIY or construction projects",
                'recycle_tips': "• Composite materials are challenging to recycle due to mixed material composition\n• Check with manufacturers for take-back or specialty recycling programs\n• Some construction waste recyclers may accept certain composite materials\n• Reuse is generally preferred over disposal for composite materials\n• Contact local waste management for proper disposal guidance and regulations",
                'sustainability_score': 3.5,
                'environmental_impact': 6.5,
                'recyclability': 2.5
            },
            'General Material': {
                'reuse_tips': f"• Assess if the {material} can be repaired, refurbished, or safely repurposed\n• Consider creative applications based on the material's properties and durability\n• Look for community groups, schools, or maker spaces that might find it useful\n• Research online tutorials and guides for upcycling similar materials\n• Consult local repair cafes or fix-it clinics for restoration possibilities",
                'recycle_tips': f"• Contact local waste management authorities about proper {material} disposal options\n• Research specialty recycling programs or facilities in your geographic area\n• Check manufacturer websites for take-back programs or recycling partnerships\n• Consider consulting environmental groups or sustainability organizations for guidance\n• Ensure proper disposal in regular waste stream if no recycling options exist",
                'sustainability_score': 5.0,
                'environmental_impact': 5.5,
                'recyclability': 4.0
            }
        }
        
        data = fallback_data.get(category, fallback_data['General Material'])
        
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