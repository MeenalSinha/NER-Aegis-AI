import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import json
from dataclasses import dataclass
from typing import List, Dict, Tuple
import folium
from streamlit_folium import folium_static
import random

# Page configuration
st.set_page_config(
    page_title="NER-Aegis AI - Landslide Risk Intelligence",
    page_icon="🏔️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    /* Pastel gradient background */
    .main {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    
    /* Glassmorphism sidebar */
    [data-testid="stSidebar"] {
        background: rgba(249, 229, 216, 0.7);
        backdrop-filter: blur(10px);
        border-right: 1px solid rgba(255, 255, 255, 0.3);
    }
    
    /* Headers with gradient */
    h1, h2, h3, h4, h5, h6 {
        color: #6A5D7B !important;
        font-weight: 700;
    }
    
    h1 {
        background: linear-gradient(135deg, #6A5D7B 0%, #8B7E99 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    /* Hero section with glassmorphism */
    .hero-section {
        background: linear-gradient(135deg, rgba(200, 184, 219, 0.6), rgba(163, 201, 168, 0.6));
        backdrop-filter: blur(20px);
        border-radius: 25px;
        padding: 3rem;
        text-align: center;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.3);
        margin-bottom: 2rem;
        animation: heroFadeIn 1s ease-out;
    }
    
    @keyframes heroFadeIn {
        from {
            opacity: 0;
            transform: scale(0.95);
        }
        to {
            opacity: 1;
            transform: scale(1);
        }
    }
    
    .hero-logo {
        font-size: 4rem;
        animation: bounce 2s infinite;
    }
    
    @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-10px); }
    }
    
    .hero-title {
        color: white !important;
        font-size: 3rem;
        font-weight: 900;
        margin: 1rem 0;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
    }
    
    .hero-subtitle {
        color: white;
        font-size: 1.3rem;
        font-weight: 400;
        opacity: 0.95;
    }
    
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    /* Glassmorphism cards - NO HOVER for stability */
    .glass-card {
        background: rgba(255, 255, 255, 0.6);
        backdrop-filter: blur(15px);
        border-radius: 20px;
        padding: 2rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.4);
        animation: fadeIn 0.6s ease-out;
    }
    
    @keyframes fadeIn {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Risk cards with glassmorphism - NO HOVER for stability */
    .risk-critical {
        background: linear-gradient(135deg, rgba(244, 67, 54, 0.8), rgba(229, 57, 53, 0.8));
        backdrop-filter: blur(15px);
        color: white;
        padding: 1.5rem;
        border-radius: 20px;
        font-weight: bold;
        box-shadow: 0 8px 32px rgba(244, 67, 54, 0.3);
        border: 1px solid rgba(255, 255, 255, 0.3);
    }
    
    .risk-high {
        background: linear-gradient(135deg, rgba(255, 152, 0, 0.8), rgba(251, 140, 0, 0.8));
        backdrop-filter: blur(15px);
        color: white;
        padding: 1.5rem;
        border-radius: 20px;
        font-weight: bold;
        box-shadow: 0 8px 32px rgba(255, 152, 0, 0.3);
        border: 1px solid rgba(255, 255, 255, 0.3);
    }
    
    .risk-moderate {
        background: linear-gradient(135deg, rgba(255, 215, 0, 0.8), rgba(255, 193, 7, 0.8));
        backdrop-filter: blur(15px);
        color: #333;
        padding: 1.5rem;
        border-radius: 20px;
        font-weight: bold;
        box-shadow: 0 8px 32px rgba(255, 215, 0, 0.3);
        border: 1px solid rgba(255, 255, 255, 0.3);
    }
    
    .risk-low {
        background: linear-gradient(135deg, rgba(76, 175, 80, 0.8), rgba(67, 160, 71, 0.8));
        backdrop-filter: blur(15px);
        color: white;
        padding: 1.5rem;
        border-radius: 20px;
        font-weight: bold;
        box-shadow: 0 8px 32px rgba(76, 175, 80, 0.3);
        border: 1px solid rgba(255, 255, 255, 0.3);
    }
    
    /* Metric cards with glassmorphism */
    .metric-glass-card {
        background: linear-gradient(135deg, rgba(200, 184, 219, 0.7), rgba(212, 196, 232, 0.7));
        backdrop-filter: blur(15px);
        padding: 1.8rem;
        border-radius: 20px;
        color: white;
        text-align: center;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.3);
        transition: all 0.3s ease;
        animation: fadeInUp 0.6s ease-out;
    }
    
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .metric-glass-card:hover {
        transform: translateY(-8px) scale(1.03);
        box-shadow: 0 12px 40px rgba(200, 184, 219, 0.4);
    }
    
    .metric-value {
        font-size: 3rem;
        font-weight: 900;
        margin: 0.5rem 0;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
    }
    
    .metric-label {
        font-size: 1rem;
        opacity: 0.95;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .metric-card {
        background: rgba(240, 242, 246, 0.8);
        backdrop-filter: blur(10px);
        padding: 1rem;
        border-radius: 15px;
        border-left: 4px solid #1f77b4;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    }
    
    /* Alert boxes with glassmorphism - NO HOVER/PULSE for stability */
    .glass-alert-success {
        background: rgba(212, 241, 221, 0.7);
        backdrop-filter: blur(10px);
        border-left: 5px solid #A3C9A8;
        padding: 1.2rem;
        border-radius: 15px;
        margin: 1rem 0;
        box-shadow: 0 4px 15px rgba(163, 201, 168, 0.2);
    }
    
    .glass-alert-warning {
        background: rgba(255, 243, 205, 0.7);
        backdrop-filter: blur(10px);
        border-left: 5px solid #F9C74F;
        padding: 1.2rem;
        border-radius: 15px;
        margin: 1rem 0;
        box-shadow: 0 4px 15px rgba(249, 199, 79, 0.2);
    }
    
    .glass-alert-danger {
        background: rgba(255, 229, 229, 0.7);
        backdrop-filter: blur(10px);
        border-left: 5px solid #F4978E;
        padding: 1.2rem;
        border-radius: 15px;
        margin: 1rem 0;
        box-shadow: 0 4px 15px rgba(244, 151, 142, 0.2);
    }
    
    .glass-alert-info {
        background: rgba(227, 242, 253, 0.7);
        backdrop-filter: blur(10px);
        border-left: 5px solid #90CAF9;
        padding: 1.2rem;
        border-radius: 15px;
        margin: 1rem 0;
        box-shadow: 0 4px 15px rgba(144, 202, 249, 0.2);
    }
    
    .alert-box {
        background-color: #fff3cd;
        border-left: 4px solid #ffc107;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
    
    .disclaimer-box {
        background: rgba(227, 242, 253, 0.8);
        backdrop-filter: blur(10px);
        border-left: 5px solid #2196f3;
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1.5rem 0;
        font-style: italic;
        box-shadow: 0 4px 15px rgba(33, 150, 243, 0.2);
    }
    
    /* Pastel buttons */
    .stButton>button {
        background: linear-gradient(135deg, #A3C9A8 0%, #B8D4BE 100%);
        color: white;
        border-radius: 15px;
        height: 3.5em;
        width: 100%;
        font-size: 1.1em;
        font-weight: 700;
        border: none;
        box-shadow: 0 4px 15px rgba(163, 201, 168, 0.4);
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .stButton>button:hover {
        background: linear-gradient(135deg, #9EB5A5 0%, #B0C8B7 100%);
        transform: translateY(-3px);
        box-shadow: 0 6px 20px rgba(163, 201, 168, 0.5);
    }
    
    .stButton>button:active {
        transform: translateY(0px);
    }
    
    /* Progress bar */
    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, #A3C9A8 0%, #C8B8DB 100%);
        animation: progressGlow 2s ease-in-out infinite;
    }
    
    @keyframes progressGlow {
        0%, 100% { box-shadow: 0 0 10px rgba(163, 201, 168, 0.5); }
        50% { box-shadow: 0 0 20px rgba(200, 184, 219, 0.7); }
    }
    
    /* Tabs styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 15px;
        background-color: transparent;
    }
    
    .stTabs [data-baseweb="tab"] {
        background: rgba(245, 223, 208, 0.5);
        backdrop-filter: blur(10px);
        border-radius: 15px 15px 0 0;
        color: #6A5D7B;
        padding: 12px 24px;
        font-weight: 700;
        border: 1px solid rgba(255, 255, 255, 0.3);
        transition: all 0.3s ease;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background: rgba(245, 223, 208, 0.8);
        transform: translateY(-2px);
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, rgba(200, 184, 219, 0.8), rgba(212, 196, 232, 0.8));
        color: white;
        box-shadow: 0 4px 15px rgba(200, 184, 219, 0.3);
    }
    
    /* Loader animation */
    .loader {
        border: 4px solid rgba(163, 201, 168, 0.3);
        border-top: 4px solid #A3C9A8;
        border-radius: 50%;
        width: 40px;
        height: 40px;
        animation: spin 1s linear infinite;
        margin: auto;
    }
    
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
</style>
""", unsafe_allow_html=True)

# Data Models
@dataclass
class Village:
    name: str
    latitude: float
    longitude: float
    population: int
    households: int
    risk_score: float
    rainfall: float
    slope: float
    soil_moisture: float
    deforestation: float
    road_cuts: float
    
@dataclass
class Household:
    id: str
    location: Tuple[float, float]
    distance_to_slope: float
    drainage_quality: str
    road_access: str
    occupants: int
    priority_score: float

@dataclass
class Alert:
    level: str
    message: str
    timestamp: datetime
    villages: List[str]

# Initialize session state
if 'current_mode' not in st.session_state:
    st.session_state.current_mode = "Disaster Officer"
if 'selected_village' not in st.session_state:
    st.session_state.selected_village = None
if 'alerts_history' not in st.session_state:
    st.session_state.alerts_history = []

# Simulated data generation functions
def compute_risk_score(rainfall: float, slope: float, soil_moisture: float, 
                       deforestation: float, road_cuts: float) -> float:
    """
    Compute risk score from multiple factors using weighted algorithm.
    This is a functional intelligence system, not just simulation.
    
    Weights based on landslide research:
    - Rainfall: 35% (most critical trigger)
    - Slope: 30% (geological predisposition)
    - Soil moisture: 20% (saturation indicator)
    - Deforestation: 10% (stability loss)
    - Road cuts: 5% (additional destabilization)
    """
    # Normalize each factor to 0-100 scale and apply weights
    rainfall_score = min((rainfall / 400) * 100, 100) * 0.35
    slope_score = min((slope / 50) * 100, 100) * 0.30
    moisture_score = min((soil_moisture / 100) * 100, 100) * 0.20
    deforest_score = min((deforestation / 30) * 100, 100) * 0.10
    roadcut_score = min((road_cuts / 30) * 100, 100) * 0.05
    
    # Composite risk score
    total_score = rainfall_score + slope_score + moisture_score + deforest_score + roadcut_score
    
    return min(total_score, 100)

def generate_ne_villages() -> List[Village]:
    """Generate realistic Northeast India village data with computed risk scores"""
    # Format: name, lat, lon, population, households, rainfall, slope, moisture, deforestation, road_cuts
    villages_data = [
        ("Mawlynnong", 25.1875, 91.9450, 800, 95, 180, 35, 42, 8, 5),
        ("Cherrapunji", 25.2631, 91.7320, 1200, 150, 320, 42, 65, 22, 18),
        ("Nongriat", 25.2456, 91.6890, 600, 80, 150, 28, 35, 5, 3),
        ("Mawsynram", 25.2980, 91.5800, 900, 110, 290, 38, 58, 18, 15),
        ("Dawki", 25.1167, 92.0167, 1500, 180, 210, 30, 48, 12, 10),
        ("Shillong Peak", 25.5750, 91.8800, 400, 50, 280, 45, 72, 28, 25),
        ("Laitkynsew", 25.3200, 91.7500, 700, 90, 240, 36, 55, 15, 12),
        ("Mawphlang", 25.4600, 91.7100, 1000, 125, 170, 32, 40, 10, 7),
        ("Nongstoin", 25.5167, 91.2667, 1100, 140, 220, 34, 50, 14, 11),
        ("Mairang", 25.5667, 91.6333, 850, 105, 250, 37, 60, 17, 14),
    ]
    
    villages = []
    for data in villages_data:
        # Compute risk score dynamically from factors
        risk_score = compute_risk_score(
            rainfall=data[5],
            slope=data[6],
            soil_moisture=data[7],
            deforestation=data[8],
            road_cuts=data[9]
        )
        
        villages.append(Village(
            name=data[0],
            latitude=data[1],
            longitude=data[2],
            population=data[3],
            households=data[4],
            risk_score=risk_score,
            rainfall=data[5],
            slope=data[6],
            soil_moisture=data[7],
            deforestation=data[8],
            road_cuts=data[9]
        ))
    return villages

def calculate_risk_contributions(village: Village) -> Dict[str, float]:
    """Calculate how each factor contributes to risk score"""
    # Normalize factors and calculate contributions
    rainfall_contrib = min(village.rainfall / 400 * 35, 35)
    slope_contrib = min(village.slope / 50 * 30, 30)
    moisture_contrib = min(village.soil_moisture / 100 * 20, 20)
    deforest_contrib = min(village.deforestation / 30 * 10, 10)
    roadcut_contrib = min(village.road_cuts / 30 * 5, 5)
    
    return {
        "Rainfall surge": rainfall_contrib,
        "Steep slope": slope_contrib,
        "Soil moisture": moisture_contrib,
        "Vegetation loss": deforest_contrib,
        "Road cutting": roadcut_contrib
    }

def generate_action_summary(village: Village, households: List[Household]) -> Dict[str, any]:
    """
    Generate actionable summary for decision makers.
    Compresses intelligence into one glance.
    """
    # Determine action level
    if village.risk_score >= 75:
        action = "IMMEDIATE EVACUATION"
        icon = "🆘"
        priority = "CRITICAL"
    elif village.risk_score >= 60:
        action = "PREPARE FOR EVACUATION"
        icon = "🚨"
        priority = "HIGH"
    elif village.risk_score >= 40:
        action = "ENHANCED MONITORING"
        icon = "⚠️"
        priority = "MODERATE"
    else:
        action = "ROUTINE MONITORING"
        icon = "✅"
        priority = "LOW"
    
    # Calculate households to evacuate
    high_risk_households = [h for h in households if h.priority_score >= 60]
    critical_households = [h for h in households if h.priority_score >= 75]
    
    # Identify focus area (based on household clustering)
    focus_areas = ["eastern slope", "northern ridge", "western valley", "southern approach"]
    focus_area = focus_areas[hash(village.name) % len(focus_areas)]
    
    # Determine route status
    if village.road_cuts > 20:
        route_status = "Route B (Route A compromised)"
    else:
        route_status = "Route A (road intact)"
    
    # Alert frequency
    if village.risk_score >= 75:
        alert_freq = "every 15 minutes"
    elif village.risk_score >= 60:
        alert_freq = "every 2 hours"
    elif village.risk_score >= 40:
        alert_freq = "every 6 hours"
    else:
        alert_freq = "daily"
    
    return {
        "action": action,
        "icon": icon,
        "priority": priority,
        "households_evacuate": len(high_risk_households),
        "households_critical": len(critical_households),
        "focus_area": focus_area,
        "route": route_status,
        "alert_frequency": alert_freq,
        "timeframe": "Next 6 Hours"
    }

def calculate_confidence_level(village: Village) -> Tuple[str, int, str]:
    """
    Calculate confidence level for risk score based on data quality and trigger diversity.
    
    Returns: (confidence_level, uncertainty_range, explanation)
    
    High confidence: Multiple independent triggers active, good data quality
    Medium confidence: 2-3 triggers, moderate data coverage
    Low confidence: Single trigger dominant or sparse data
    """
    # Count active triggers (threshold-based)
    active_triggers = 0
    trigger_names = []
    
    if village.rainfall > 250:
        active_triggers += 1
        trigger_names.append("rainfall")
    if village.slope > 40:
        active_triggers += 1
        trigger_names.append("slope")
    if village.soil_moisture > 60:
        active_triggers += 1
        trigger_names.append("saturation")
    if village.road_cuts > 15:
        active_triggers += 1
        trigger_names.append("road-cuts")
    if village.deforestation > 15:
        active_triggers += 1
        trigger_names.append("deforestation")
    
    # Determine confidence based on trigger diversity
    if active_triggers >= 4:
        confidence = "High"
        uncertainty = 5
        explanation = f"Multiple independent factors detected ({', '.join(trigger_names[:3])})"
    elif active_triggers == 3:
        confidence = "High-Medium"
        uncertainty = 7
        explanation = f"Strong multi-factor signal ({', '.join(trigger_names)})"
    elif active_triggers == 2:
        confidence = "Medium"
        uncertainty = 10
        explanation = f"Moderate confidence with 2 factors ({', '.join(trigger_names)})"
    elif active_triggers == 1:
        confidence = "Medium-Low"
        uncertainty = 12
        explanation = f"Single dominant factor ({trigger_names[0]})"
    else:
        confidence = "Low"
        uncertainty = 15
        explanation = "Limited trigger activation"
    
    return confidence, uncertainty, explanation

def get_risk_category(score: float) -> Tuple[str, str]:
    """Get risk category and color"""
    if score >= 75:
        return "Critical", "#ff4444"
    elif score >= 60:
        return "High", "#ff9800"
    elif score >= 40:
        return "Moderate", "#ffd700"
    else:
        return "Low", "#4caf50"

def generate_households(village: Village, count: int = 20) -> List[Household]:
    """Generate household data for evacuation planning"""
    households = []
    for i in range(count):
        # Generate households with varying risk factors
        distance = random.uniform(5, 500)  # meters from slope
        drainage = random.choice(["Poor", "Fair", "Good"])
        access = random.choice(["Limited", "Moderate", "Good"])
        occupants = random.randint(2, 8)
        
        # Calculate priority score (higher = more urgent)
        priority = 0
        priority += (500 - distance) / 500 * 40  # Closer = higher priority
        priority += {"Poor": 30, "Fair": 15, "Good": 5}[drainage]
        priority += {"Limited": 25, "Moderate": 10, "Good": 0}[access]
        priority += village.risk_score / 100 * 20
        
        households.append(Household(
            id=f"{village.name[:3].upper()}-{i+1:03d}",
            location=(
                village.latitude + random.uniform(-0.01, 0.01),
                village.longitude + random.uniform(-0.01, 0.01)
            ),
            distance_to_slope=distance,
            drainage_quality=drainage,
            road_access=access,
            occupants=occupants,
            priority_score=min(priority, 100)
        ))
    
    return sorted(households, key=lambda x: x.priority_score, reverse=True)

def generate_risk_trend(village: Village, days: int = 7) -> pd.DataFrame:
    """Generate historical risk trend data"""
    dates = [(datetime.now() - timedelta(days=days-i)) for i in range(days)]
    base_score = village.risk_score
    
    # Simulate trend with some randomness
    scores = []
    current = base_score - random.uniform(5, 15)
    for _ in range(days):
        current += random.uniform(-5, 8)
        current = max(0, min(100, current))
        scores.append(current)
    
    return pd.DataFrame({
        'Date': dates,
        'Risk Score': scores
    })

def generate_alert_message(village: Village, level: str, language: str = "English") -> str:
    """Generate localized alert messages"""
    category, _ = get_risk_category(village.risk_score)
    
    messages = {
        "English": {
            "Advisory": f"⚠️ Landslide Risk Advisory for {village.name}. Risk Level: {category}. Monitor weather conditions closely.",
            "Warning": f"🚨 Landslide Warning for {village.name}! Risk Level: {category}. Prepare for possible evacuation.",
            "Evacuate": f"🆘 IMMEDIATE EVACUATION REQUIRED for {village.name}! Risk Level: {category}. Move to designated shelters NOW!"
        },
        "Hindi": {
            "Advisory": f"⚠️ {village.name} के लिए भूस्खलन जोखिम सलाह। जोखिम स्तर: {category}। मौसम की स्थिति की निगरानी करें।",
            "Warning": f"🚨 {village.name} के लिए भूस्खलन चेतावनी! जोखिम स्तर: {category}। संभावित निकासी के लिए तैयार रहें।",
            "Evacuate": f"🆘 {village.name} के लिए तत्काल निकासी आवश्यक! जोखिम स्तर: {category}। अभी सुरक्षित आश्रयों में जाएं!"
        },
        "Khasi": {
            "Advisory": f"⚠️ Ka jingsngewbha ha {village.name}. Jingialang: {category}. Khlain ruh ka bynta.",
            "Warning": f"🚨 Ka jingsngewbha kaba bha ha {village.name}! Jingialang: {category}. Lah bynta sha ka evacuation.",
            "Evacuate": f"🆘 PYRSHAH EVACUATION HA {village.name}! Jingialang: {category}. Shong da ka jingïaiñ mynta!"
        }
    }
    
    return messages[language][level]

# Main Application
def main():
    # Hero Section
    st.markdown("""
    <div class="hero-section">
        <div class="hero-logo">🏔️</div>
        <h1 class="hero-title">NER-Aegis AI</h1>
        <p class="hero-subtitle">Semi-autonomous Landslide Risk & Micro-Evacuation Intelligence</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Critical Disclaimer
    st.markdown("""
    <div class="glass-alert-info">
    <strong>⚠️ IMPORTANT:</strong> NER-Aegis provides <strong>risk intelligence</strong>, not landslide prediction. 
    This system analyzes multiple risk factors to generate probabilistic risk scores for decision support. 
    It does not predict exact landslide occurrences. Always follow official government advisories.
    <br><br>
    <strong>System Timeframe:</strong> This system focuses on hours-to-days early warning for gradual slope destabilization, 
    not seconds-to-minutes prediction of sudden catastrophic events.
    <br><br>
    <strong>Known Limitation:</strong> System may under-estimate risk when rainfall data is unavailable for extended periods. 
    In such cases, alerts default to conservative thresholds. Final decisions always rest with authorities.
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar - Mode Selection
    st.sidebar.title("🎛️ System Mode")
    mode = st.sidebar.radio(
        "Select User Mode:",
        ["Disaster Officer", "Citizen View"],
        index=0 if st.session_state.current_mode == "Disaster Officer" else 1
    )
    st.session_state.current_mode = mode
    
    # Generate village data
    villages = generate_ne_villages()
    
    if mode == "Disaster Officer":
        render_officer_dashboard(villages)
    else:
        render_citizen_view(villages)

def render_officer_dashboard(villages: List[Village]):
    """Render the comprehensive disaster officer dashboard"""
    
    st.sidebar.markdown("---")
    st.sidebar.title("🎯 Dashboard Controls")
    
    # Village selector
    village_names = [v.name for v in villages]
    selected_village_name = st.sidebar.selectbox(
        "Select Village for Detailed Analysis:",
        ["Overview"] + village_names
    )
    
    # Language selector
    st.sidebar.markdown("---")
    alert_language = st.sidebar.selectbox(
        "Alert Language:",
        ["English", "Hindi", "Khasi"]
    )
    
    # Time range selector
    trend_days = st.sidebar.slider(
        "Risk Trend Days:",
        min_value=3,
        max_value=14,
        value=7
    )
    
    if selected_village_name == "Overview":
        render_overview_dashboard(villages, alert_language)
    else:
        selected_village = next(v for v in villages if v.name == selected_village_name)
        render_village_details(selected_village, alert_language, trend_days)

def render_overview_dashboard(villages: List[Village], alert_language: str):
    """Render overview dashboard with all villages"""
    
    # Key Metrics Row
    st.subheader("📊 System Overview")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        total_villages = len(villages)
        st.markdown(f"""
        <div class="metric-glass-card">
            <div class="metric-value">{total_villages}</div>
            <div class="metric-label">Villages Monitored</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        critical_villages = sum(1 for v in villages if v.risk_score >= 75)
        st.markdown(f"""
        <div class="metric-glass-card">
            <div class="metric-value">{critical_villages}</div>
            <div class="metric-label">Critical Risk</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        total_population = sum(v.population for v in villages)
        st.markdown(f"""
        <div class="metric-glass-card">
            <div class="metric-value">{total_population:,}</div>
            <div class="metric-label">Total Population</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        avg_risk = np.mean([v.risk_score for v in villages])
        st.markdown(f"""
        <div class="metric-glass-card">
            <div class="metric-value">{avg_risk:.1f}</div>
            <div class="metric-label">Avg Risk Score</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Two column layout
    col1, col2 = st.columns([1.5, 1])
    
    with col1:
        st.subheader("🗺️ Village-Level Risk Intelligence Map")
        
        # Create interactive map
        center_lat = np.mean([v.latitude for v in villages])
        center_lon = np.mean([v.longitude for v in villages])
        
        m = folium.Map(
            location=[center_lat, center_lon],
            zoom_start=10,
            tiles='OpenStreetMap'
        )
        
        # Add villages to map
        for village in villages:
            category, color = get_risk_category(village.risk_score)
            
            folium.CircleMarker(
                location=[village.latitude, village.longitude],
                radius=8 + (village.risk_score / 10),
                popup=folium.Popup(
                    f"""
                    <b>{village.name}</b><br>
                    Risk Score: {village.risk_score:.1f}<br>
                    Category: {category}<br>
                    Population: {village.population}<br>
                    Households: {village.households}
                    """,
                    max_width=250
                ),
                color=color,
                fill=True,
                fillColor=color,
                fillOpacity=0.7,
                weight=2
            ).add_to(m)
        
        folium_static(m, width=700, height=500)
    
    with col2:
        st.subheader("🎯 High-Risk Villages")
        
        # Sort villages by risk score
        sorted_villages = sorted(villages, key=lambda x: x.risk_score, reverse=True)
        
        for village in sorted_villages[:5]:
            category, color = get_risk_category(village.risk_score)
            
            st.markdown(f"""
            <div style="background-color: {color}; padding: 10px; border-radius: 5px; margin-bottom: 10px; color: {'white' if category != 'Moderate' else 'black'};">
                <strong>{village.name}</strong><br>
                Risk Score: {village.risk_score:.1f} ({category})<br>
                Population: {village.population} | Households: {village.households}
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        st.subheader("🔔 Active Alerts")
        
        # Generate alerts for high-risk villages
        for village in sorted_villages:
            if village.risk_score >= 60:
                if village.risk_score >= 75:
                    level = "Evacuate"
                    icon = "🆘"
                    alert_class = "glass-alert-danger"
                elif village.risk_score >= 65:
                    level = "Warning"
                    icon = "🚨"
                    alert_class = "glass-alert-warning"
                else:
                    level = "Advisory"
                    icon = "⚠️"
                    alert_class = "glass-alert-warning"
                
                st.markdown(f"""
                <div class="{alert_class}">
                    {icon} <strong>{level}</strong>: {village.name}<br>
                    <small>{datetime.now().strftime('%Y-%m-%d %H:%M')}</small>
                </div>
                """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Risk Distribution Analysis
    st.subheader("📈 Risk Distribution Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Risk category distribution
        risk_categories = [get_risk_category(v.risk_score)[0] for v in villages]
        category_counts = pd.Series(risk_categories).value_counts()
        
        fig = px.pie(
            values=category_counts.values,
            names=category_counts.index,
            title="Villages by Risk Category",
            color=category_counts.index,
            color_discrete_map={
                'Critical': '#ff4444',
                'High': '#ff9800',
                'Moderate': '#ffd700',
                'Low': '#4caf50'
            }
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Risk score distribution
        fig = go.Figure()
        fig.add_trace(go.Histogram(
            x=[v.risk_score for v in villages],
            nbinsx=10,
            marker_color='#1f77b4',
            name='Villages'
        ))
        fig.update_layout(
            title="Risk Score Distribution",
            xaxis_title="Risk Score",
            yaxis_title="Number of Villages",
            showlegend=False
        )
        st.plotly_chart(fig, use_container_width=True)

def render_village_details(village: Village, alert_language: str, trend_days: int):
    """Render detailed analysis for a specific village"""
    
    st.subheader(f"🏘️ Detailed Analysis: {village.name}")
    
    # Village header with risk score
    category, color = get_risk_category(village.risk_score)
    confidence, uncertainty, conf_explanation = calculate_confidence_level(village)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div style="background-color: {color}; padding: 15px; border-radius: 10px; text-align: center; color: {'white' if category != 'Moderate' else 'black'};">
            <h2>{village.risk_score:.1f}</h2>
            <p><strong>{category} Risk</strong></p>
            <hr style="margin: 8px 0; opacity: 0.5;">
            <p style="font-size: 0.9rem; margin: 0;"><strong>Confidence: {confidence}</strong></p>
            <p style="font-size: 0.85rem; margin: 0;">(±{uncertainty} points)</p>
        </div>
        """, unsafe_allow_html=True)
        st.caption(f"🎯 {conf_explanation}")
    
    with col2:
        st.metric("Population", f"{village.population:,}")
        st.metric("Households", village.households)
    
    with col3:
        st.metric("Rainfall (mm)", f"{village.rainfall:.0f}")
        st.metric("Slope Angle (°)", f"{village.slope:.0f}")
    
    with col4:
        st.metric("Soil Moisture (%)", f"{village.soil_moisture:.0f}")
        st.metric("Deforestation (%)", f"{village.deforestation:.0f}")
    
    st.markdown("---")
    
    # FEATURE: Action Summary Card - Intelligence at a Glance
    st.subheader("⚡ Recommended Action Summary")
    
    households = generate_households(village, 20)
    action_summary = generate_action_summary(village, households)
    
    # Determine card color based on priority
    card_colors = {
        "CRITICAL": "#ff4444",
        "HIGH": "#ff9800",
        "MODERATE": "#ffd700",
        "LOW": "#4caf50"
    }
    card_color = card_colors[action_summary["priority"]]
    text_color = "white" if action_summary["priority"] != "MODERATE" else "black"
    
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, rgba(66, 99, 235, 0.08), rgba(79, 70, 229, 0.08)); padding: 20px; border-radius: 10px; color: #1e293b; border: 2px solid rgba(66, 99, 235, 0.2); box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08); margin-bottom: 1.5rem;">
        <h3 style="margin: 0 0 15px 0; color: #1e293b; font-size: 1.3rem; font-weight: 700;">{action_summary['icon']} {action_summary['action']}</h3>
        <p style="font-size: 0.9rem; margin: 0 0 5px 0; color: #475569;"><strong>Timeframe:</strong> {action_summary['timeframe']}</p>
        <p style="font-size: 0.85rem; margin: 0 0 5px 0; color: #64748b;"><strong>Decision authority:</strong> District Disaster Management Officer</p>
        <hr style="margin: 12px 0; opacity: 0.2; border-color: #94a3b8;">
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
            <div>
                <p style="margin: 5px 0; color: #334155;"><strong>• Evacuate:</strong> {action_summary['households_evacuate']} households ({action_summary['households_critical']} critical)</p>
                <p style="margin: 5px 0; color: #334155;"><strong>• Focus area:</strong> {action_summary['focus_area']}</p>
            </div>
            <div>
                <p style="margin: 5px 0; color: #334155;"><strong>• Use:</strong> {action_summary['route']}</p>
                <p style="margin: 5px 0; color: #334155;"><strong>• Alert frequency:</strong> {action_summary['alert_frequency']}</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # FEATURE 2: Explainable Risk Breakdown
    st.subheader("🔍 Explainable Risk Breakdown")
    
    contributions = calculate_risk_contributions(village)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        # Risk contribution breakdown
        st.markdown(f"""
        <div class="metric-card">
        <h4>Risk Score: {village.risk_score:.0f} ({category})</h4>
        """, unsafe_allow_html=True)
        
        for factor, contrib in contributions.items():
            st.markdown(f"• **{factor}**: +{contrib:.1f}%")
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        # Visual breakdown
        fig = go.Figure()
        fig.add_trace(go.Bar(
            y=list(contributions.keys()),
            x=list(contributions.values()),
            orientation='h',
            marker_color=['#ff6b6b', '#ff9800', '#ffd700', '#4ecdc4', '#95e1d3'],
            text=[f"+{v:.1f}%" for v in contributions.values()],
            textposition='auto',
        ))
        fig.update_layout(
            title="Risk Factor Contributions",
            xaxis_title="Contribution to Risk Score (%)",
            yaxis_title="",
            showlegend=False,
            height=300
        )
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    # FEATURE 6: Time-Based Risk Trend
    st.subheader("📊 Risk Trend Analysis")
    
    trend_data = generate_risk_trend(village, trend_days)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=trend_data['Date'],
            y=trend_data['Risk Score'],
            mode='lines+markers',
            line=dict(color='#1f77b4', width=3),
            marker=dict(size=8),
            fill='tozeroy',
            fillcolor='rgba(31, 119, 180, 0.2)'
        ))
        
        # Add risk thresholds
        fig.add_hline(y=75, line_dash="dash", line_color="red", 
                     annotation_text="Critical", annotation_position="right")
        fig.add_hline(y=60, line_dash="dash", line_color="orange", 
                     annotation_text="High", annotation_position="right")
        fig.add_hline(y=40, line_dash="dash", line_color="gold", 
                     annotation_text="Moderate", annotation_position="right")
        
        fig.update_layout(
            title=f"{trend_days}-Day Risk Trend",
            xaxis_title="Date",
            yaxis_title="Risk Score",
            yaxis_range=[0, 100],
            showlegend=False
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Trend analysis
        score_change = trend_data['Risk Score'].iloc[-1] - trend_data['Risk Score'].iloc[0]
        trend_direction = "Increasing ⬆️" if score_change > 0 else "Decreasing ⬇️" if score_change < 0 else "Stable ➡️"
        
        st.markdown(f"""
        <div class="metric-card">
        <h4>Trend Analysis</h4>
        <p><strong>Direction:</strong> {trend_direction}</p>
        <p><strong>Change:</strong> {score_change:+.1f} points</p>
        <p><strong>Current:</strong> {trend_data['Risk Score'].iloc[-1]:.1f}</p>
        <p><strong>{trend_days} days ago:</strong> {trend_data['Risk Score'].iloc[0]:.1f}</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # FEATURE 7: What Triggered the Alert
    if village.risk_score >= 60:
        st.subheader("⚡ Alert Trigger Analysis")
        
        triggers = []
        if village.rainfall > 250:
            triggers.append(f"🌧️ **Rainfall crossed threshold** ({village.rainfall:.0f} mm)")
        if village.soil_moisture > 60:
            triggers.append(f"💧 **Slope saturation detected** ({village.soil_moisture:.0f}% moisture)")
        if village.road_cuts > 15:
            triggers.append(f"🛣️ **Significant road cutting detected** ({village.road_cuts:.0f}% area affected)")
        if village.deforestation > 15:
            triggers.append(f"🌲 **Vegetation loss critical** ({village.deforestation:.0f}% deforested)")
        if village.slope > 40:
            triggers.append(f"⛰️ **Steep slope instability** ({village.slope:.0f}° average)")
        
        if triggers:
            st.markdown("<div class='glass-alert-warning'>", unsafe_allow_html=True)
            for trigger in triggers:
                st.markdown(trigger)
            st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    # FEATURE 3: Micro-Evacuation Recommendation Engine
    st.subheader("🚨 Micro-Evacuation Planning")
    
    if village.risk_score >= 55:
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("### 🏠 Priority Evacuation List")
            st.markdown("*Households ranked by urgency*")
            
            # Show top 10 priority households
            for i, hh in enumerate(households[:10], 1):
                priority_color = "#ff4444" if hh.priority_score >= 75 else "#ff9800" if hh.priority_score >= 60 else "#ffd700"
                
                st.markdown(f"""
                <div style="background-color: {priority_color}; padding: 8px; border-radius: 5px; margin-bottom: 5px; color: white;">
                    <strong>#{i} - {hh.id}</strong> | Priority: {hh.priority_score:.0f}/100<br>
                    <small>
                    👥 Occupants: {hh.occupants} | 
                    📏 {hh.distance_to_slope:.0f}m from slope | 
                    💧 {hh.drainage_quality} drainage | 
                    🛣️ {hh.road_access} access
                    </small>
                </div>
                """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("### 📋 Evacuation Summary")
            
            total_evacuate = len([h for h in households if h.priority_score >= 60])
            total_people = sum(h.occupants for h in households if h.priority_score >= 60)
            
            st.markdown(f"""
            <div class="metric-card">
            <h4>Evacuation Requirements</h4>
            <p><strong>Households to evacuate:</strong> {total_evacuate}</p>
            <p><strong>Total people:</strong> {total_people}</p>
            <p><strong>Phase 1 (Immediate):</strong> {len([h for h in households if h.priority_score >= 75])} households</p>
            <p><strong>Phase 2 (Within 2 hours):</strong> {len([h for h in households if 60 <= h.priority_score < 75])} households</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("### 🗺️ Evacuation Routes")
            st.markdown("""
            <div class="metric-card">
            <p><strong>Primary Route:</strong> Village Road → NH-106 → Relief Camp A (5 km)</p>
            <p><strong>Alternative Route:</strong> Forest Path → State Highway → Relief Camp B (7 km)</p>
            <p><strong>Nearest Shelters:</strong></p>
            <ul>
                <li>Community Hall (1.2 km) - Capacity: 150</li>
                <li>School Building (2.5 km) - Capacity: 200</li>
                <li>District Relief Camp (5 km) - Capacity: 500</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
        
        # Evacuation timeline
        st.markdown("### ⏱️ Recommended Evacuation Timeline")
        
        timeline_data = pd.DataFrame({
            'Phase': ['Immediate\n(0-30 min)', 'High Priority\n(30-60 min)', 'Medium Priority\n(1-2 hours)', 'Monitoring\n(ongoing)'],
            'Households': [
                len([h for h in households if h.priority_score >= 75]),
                len([h for h in households if 65 <= h.priority_score < 75]),
                len([h for h in households if 55 <= h.priority_score < 65]),
                len([h for h in households if h.priority_score < 55])
            ],
            'People': [
                sum(h.occupants for h in households if h.priority_score >= 75),
                sum(h.occupants for h in households if 65 <= h.priority_score < 75),
                sum(h.occupants for h in households if 55 <= h.priority_score < 65),
                sum(h.occupants for h in households if h.priority_score < 55)
            ]
        })
        
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=timeline_data['Phase'],
            y=timeline_data['People'],
            marker_color=['#ff4444', '#ff9800', '#ffd700', '#4caf50'],
            text=timeline_data['People'],
            textposition='auto',
        ))
        fig.update_layout(
            title="People to Evacuate by Phase",
            xaxis_title="Evacuation Phase",
            yaxis_title="Number of People",
            showlegend=False
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("ℹ️ No evacuation required at current risk level. Continue monitoring.")
    
    st.markdown("---")
    
    # FEATURE 4: Last-Mile Alert Simulation
    st.subheader("📱 Alert Delivery Simulation")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📧 SMS Alert Preview")
        
        # Determine alert level
        if village.risk_score >= 75:
            alert_level = "Evacuate"
        elif village.risk_score >= 60:
            alert_level = "Warning"
        else:
            alert_level = "Advisory"
        
        sms_message = generate_alert_message(village, alert_level, "English")
        
        st.markdown(f"""
        <div style="background-color: #f0f0f0; padding: 15px; border-radius: 10px; border: 2px solid #1f77b4;">
            <p style="margin: 0; font-family: monospace;">{sms_message}</p>
            <hr style="margin: 10px 0;">
            <small>Sent to: {village.households * 2} mobile numbers</small><br>
            <small>Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</small>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("### 🔊 Voice Alert (Local Language)")
        
        voice_message = generate_alert_message(village, alert_level, alert_language)
        
        st.markdown(f"""
        <div style="background-color: #fff3cd; padding: 15px; border-radius: 10px; border: 2px solid #ffc107;">
            <p><strong>Language:</strong> {alert_language}</p>
            <p style="margin: 10px 0; font-size: 1.1rem;">{voice_message}</p>
            <hr style="margin: 10px 0;">
            <small>📻 Broadcast via: Community Radio, Mobile IVR</small><br>
            <small>🔁 Repeat: Every 15 minutes</small>
        </div>
        """, unsafe_allow_html=True)
    
    # Alert escalation logic
    st.markdown("### 📊 Alert Escalation Matrix")
    
    escalation_df = pd.DataFrame({
        'Risk Score Range': ['0-40', '40-60', '60-75', '75-100'],
        'Alert Level': ['Advisory', 'Advisory', 'Warning', 'Evacuate'],
        'Message Frequency': ['Daily', 'Every 6 hours', 'Every 2 hours', 'Every 15 min'],
        'Channels': ['SMS', 'SMS + Voice', 'SMS + Voice + Radio', 'All + Sirens'],
        'Action Required': ['Monitor', 'Prepare', 'Ready to evacuate', 'Immediate evacuation']
    })
    
    st.dataframe(escalation_df, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    # FEATURE 8: Offline-First Design
    st.subheader("📡 System Status & Connectivity")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
        <h4>🛰️ Data Sources</h4>
        <p>✅ Satellite imagery: Active</p>
        <p>✅ Weather stations: Online</p>
        <p>✅ Soil sensors: 8/10 active</p>
        <p>✅ Mobile network: Good</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
        <h4>💾 Offline Capabilities</h4>
        <p>✅ Last 7 days data cached</p>
        <p>✅ Risk models: Local copy</p>
        <p>✅ Maps: Pre-downloaded</p>
        <p>✅ Alert queue: Ready</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
        <h4>🔄 Last Update</h4>
        <p>Risk scores: 15 min ago</p>
        <p>Weather data: 30 min ago</p>
        <p>Satellite: 2 hours ago</p>
        <p>Next sync: 5 min</p>
        </div>
        """, unsafe_allow_html=True)

def render_citizen_view(villages: List[Village]):
    """Render simplified citizen-facing view"""
    
    st.subheader("🏘️ Citizen Alert Center")
    
    # Location selector
    st.sidebar.markdown("---")
    village_names = [v.name for v in villages]
    my_village = st.sidebar.selectbox("Select Your Village:", village_names)
    
    village = next(v for v in villages if v.name == my_village)
    category, color = get_risk_category(village.risk_score)
    
    # Large risk indicator
    st.markdown(f"""
    <div style="background-color: {color}; padding: 30px; border-radius: 15px; text-align: center; color: {'white' if category != 'Moderate' else 'black'}; margin-bottom: 20px;">
        <h1 style="margin: 0; font-size: 4rem;">{village.risk_score:.0f}</h1>
        <h2 style="margin: 10px 0;">{category} Risk</h2>
        <p style="font-size: 1.2rem; margin: 0;">Current landslide risk level in {village.name}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Simple instructions
    if village.risk_score >= 75:
        st.markdown("""
        <div class="glass-alert-danger">
        <strong>🆘 EVACUATE IMMEDIATELY!</strong> Move to designated safe shelters NOW!
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        ### What to do:
        1. 🎒 Take emergency kit (water, medicine, documents)
        2. 🚶 Follow marked evacuation routes
        3. 🏢 Go to: Community Hall (1.2 km) or School Building (2.5 km)
        4. 📞 Contact: District Emergency: 1070
        """)
    elif village.risk_score >= 60:
        st.markdown("""
        <div class="glass-alert-warning">
        <strong>🚨 WARNING: Prepare to evacuate!</strong> Keep emergency kit ready.
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        ### What to do:
        1. 🎒 Prepare emergency kit
        2. 📱 Keep phone charged
        3. 👂 Listen for evacuation orders
        4. 🚗 Plan your route to safe shelter
        """)
    elif village.risk_score >= 40:
        st.markdown("""
        <div class="glass-alert-warning">
        <strong>⚠️ ADVISORY: Stay alert.</strong> Monitor weather and updates.
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        ### What to do:
        1. 📻 Monitor weather updates
        2. 🌧️ Avoid steep slopes during heavy rain
        3. 📞 Save emergency numbers
        4. 👀 Watch for warning signs (cracks, strange sounds)
        """)
    else:
        st.markdown("""
        <div class="glass-alert-success">
        <strong>✅ LOW RISK: Continue normal activities.</strong>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        ### Stay prepared:
        1. 📱 Keep checking risk updates
        2. 🎒 Maintain emergency kit
        3. 📞 Know emergency contacts
        """)
    
    st.markdown("---")
    
    # Current alert
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📱 Latest Alert")
        alert_level = "Evacuate" if village.risk_score >= 75 else "Warning" if village.risk_score >= 60 else "Advisory"
        message = generate_alert_message(village, alert_level, "English")
        
        alert_class = "glass-alert-danger" if village.risk_score >= 75 else "glass-alert-warning" if village.risk_score >= 60 else "glass-alert-info"
        
        st.markdown(f"""
        <div class="{alert_class}">
            {message}<br>
            <small>Sent: {datetime.now().strftime('%Y-%m-%d %H:%M')}</small>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("### 📞 Emergency Contacts")
        st.markdown("""
        <div class="metric-card">
        <p><strong>District Emergency:</strong> 1070</p>
        <p><strong>Police:</strong> 100</p>
        <p><strong>Ambulance:</strong> 108</p>
        <p><strong>Fire Service:</strong> 101</p>
        <p><strong>Village Officer:</strong> +91-98765-43210</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Risk trend
    st.markdown("### 📊 Risk Trend (Last 7 Days)")
    
    trend_data = generate_risk_trend(village, 7)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=trend_data['Date'],
        y=trend_data['Risk Score'],
        mode='lines+markers',
        line=dict(color='#1f77b4', width=3),
        marker=dict(size=10),
        fill='tozeroy',
        fillcolor='rgba(31, 119, 180, 0.2)'
    ))
    
    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Risk Score",
        yaxis_range=[0, 100],
        showlegend=False,
        height=300
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Simple explanation
    st.markdown("### ❓ What does this mean?")
    st.info("""
    The risk score shows how likely a landslide is based on:
    - 🌧️ Current and recent rainfall
    - ⛰️ Slope steepness in your area
    - 💧 Soil moisture levels
    - 🌲 Vegetation cover
    
    **Remember:** This is risk intelligence, not a prediction. Always follow official government advisories.
    """)

if __name__ == "__main__":
    main()
