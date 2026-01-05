"""
NER-Aegis AI - Alert Engine

This module handles alert generation, escalation, and multi-channel delivery:
- Risk-based alert level determination
- Multi-language message generation
- Escalation logic and frequency control
- Channel selection (SMS, Voice, Radio)

Engineering Principle: Progressive alert escalation with cultural sensitivity
"""

from typing import Dict, List, Tuple
from datetime import datetime


class AlertLevel:
    """Alert level constants"""
    ADVISORY = "Advisory"
    WARNING = "Warning"
    EVACUATE = "Evacuate"


def determine_alert_level(risk_score: float) -> str:
    """
    Determine appropriate alert level based on risk score.
    
    Thresholds intentionally aligned across risk, alert, and evacuation engines.
    
    Thresholds:
    - Advisory: 40-60 (monitor conditions)
    - Warning: 60-75 (prepare to evacuate)
    - Evacuate: 75+ (immediate action)
    - No Alert: <40 (routine monitoring)
    
    Args:
        risk_score: Computed risk score (0-100)
    
    Returns:
        str: Alert level (Advisory/Warning/Evacuate/No Alert)
    """
    if risk_score >= 75:
        return AlertLevel.EVACUATE
    elif risk_score >= 60:
        return AlertLevel.WARNING
    elif risk_score >= 40:
        return AlertLevel.ADVISORY
    else:
        return "No Alert"  # Explicit state for clear system behavior


def get_alert_frequency(risk_score: float) -> str:
    """
    Determine alert repetition frequency based on risk level.
    
    Args:
        risk_score: Risk score (0-100)
    
    Returns:
        str: Human-readable frequency
    """
    if risk_score >= 75:
        return "every 15 minutes"
    elif risk_score >= 60:
        return "every 2 hours"
    elif risk_score >= 40:
        return "every 6 hours"
    else:
        return "daily"


def get_delivery_channels(risk_score: float) -> List[str]:
    """
    Determine which communication channels to use based on urgency.
    
    Progressive escalation:
    - Low: SMS only
    - Moderate: SMS + Voice
    - High: SMS + Voice + Radio
    - Critical: All channels + Sirens
    
    Note: Channel availability assumed; real deployment requires authority integration.
    
    Args:
        risk_score: Risk score (0-100)
    
    Returns:
        List of channel names
    """
    if risk_score >= 75:
        return ["SMS", "Voice IVR", "Community Radio", "Emergency Sirens"]
    elif risk_score >= 60:
        return ["SMS", "Voice IVR", "Community Radio"]
    elif risk_score >= 40:
        return ["SMS", "Voice IVR"]
    else:
        return ["SMS"]


def generate_alert_message(
    village_name: str,
    risk_score: float,
    alert_level: str,
    language: str = "English"
) -> str:
    """
    Generate localized alert message for specified language.
    
    Supported languages:
    - English: Primary language
    - Hindi: Wide regional coverage
    - Khasi: Local tribal language
    
    Args:
        village_name: Name of the village
        risk_score: Risk score (0-100)
        alert_level: Advisory/Warning/Evacuate
        language: Target language
    
    Returns:
        str: Formatted alert message
    """
    from logic.risk_engine import get_risk_category
    category, _ = get_risk_category(risk_score)
    
    messages = {
        "English": {
            AlertLevel.ADVISORY: f"⚠️ Landslide Risk Advisory for {village_name}. Risk Level: {category}. Monitor weather conditions closely.",
            AlertLevel.WARNING: f"🚨 Landslide Warning for {village_name}! Risk Level: {category}. Prepare for possible evacuation.",
            AlertLevel.EVACUATE: f"IMMEDIATE EVACUATION REQUIRED for {village_name}. Risk Level: {category}. Move to designated shelters now."
        },
        "Hindi": {
            AlertLevel.ADVISORY: f"⚠️ {village_name} के लिए भूस्खलन जोखिम सलाह। जोखिम स्तर: {category}। मौसम की स्थिति की निगरानी करें।",
            AlertLevel.WARNING: f"🚨 {village_name} के लिए भूस्खलन चेतावनी! जोखिम स्तर: {category}। संभावित निकासी के लिए तैयार रहें।",
            AlertLevel.EVACUATE: f"तत्काल निकासी आवश्यक {village_name}। जोखिम स्तर: {category}। अभी सुरक्षित आश्रयों में जाएं।"
        },
        "Khasi": {
            AlertLevel.ADVISORY: f"⚠️ Ka jingsngewbha ha {village_name}. Jingialang: {category}. Khlain ruh ka bynta.",
            AlertLevel.WARNING: f"🚨 Ka jingsngewbha kaba bha ha {village_name}! Jingialang: {category}. Lah bynta sha ka evacuation.",
            AlertLevel.EVACUATE: f"PYRSHAH EVACUATION HA {village_name}. Jingialang: {category}. Shong da ka jingïaiñ mynta."
        }
    }
    
    return messages.get(language, messages["English"]).get(alert_level, "")


def create_alert_escalation_matrix() -> List[Dict[str, str]]:
    """
    Generate alert escalation matrix for reference.
    
    Returns:
        List of dicts describing escalation levels
    """
    return [
        {
            "Risk Score Range": "0-40",
            "Alert Level": "Advisory",
            "Message Frequency": "Daily",
            "Channels": "SMS",
            "Action Required": "Monitor"
        },
        {
            "Risk Score Range": "40-60",
            "Alert Level": "Advisory",
            "Message Frequency": "Every 6 hours",
            "Channels": "SMS + Voice",
            "Action Required": "Prepare"
        },
        {
            "Risk Score Range": "60-75",
            "Alert Level": "Warning",
            "Message Frequency": "Every 2 hours",
            "Channels": "SMS + Voice + Radio",
            "Action Required": "Ready to evacuate"
        },
        {
            "Risk Score Range": "75-100",
            "Alert Level": "Evacuate",
            "Message Frequency": "Every 15 min",
            "Channels": "All + Sirens",
            "Action Required": "Immediate evacuation"
        }
    ]


def generate_alert_metadata(
    village_name: str,
    risk_score: float,
    households_affected: int,
    population: int
) -> Dict[str, any]:
    """
    Generate metadata for alert tracking and logging.
    
    Args:
        village_name: Name of village
        risk_score: Current risk score
        households_affected: Number of households in alert zone
        population: Total population affected
    
    Returns:
        Dict with alert metadata
    """
    alert_level = determine_alert_level(risk_score)
    channels = get_delivery_channels(risk_score)
    frequency = get_alert_frequency(risk_score)
    
    return {
        "village": village_name,
        "timestamp": datetime.now().isoformat(),
        "risk_score": risk_score,
        "alert_level": alert_level,
        "channels": channels,
        "frequency": frequency,
        "households_affected": households_affected,
        "population_affected": population,
        "delivery_count": households_affected * 2,  # Assume 2 phone numbers per household
        "status": "active" if alert_level != "No Alert" else "monitoring"
    }


def format_sms_alert(
    village_name: str,
    risk_score: float,
    language: str = "English",
    max_length: int = 160
) -> str:
    """
    Format alert for SMS delivery (160 character limit).
    
    Args:
        village_name: Name of village
        risk_score: Current risk score
        language: Target language
        max_length: Maximum SMS length
    
    Returns:
        str: Formatted SMS message (empty if no alert needed)
    """
    alert_level = determine_alert_level(risk_score)
    if alert_level == "No Alert":
        return ""
    
    full_message = generate_alert_message(village_name, risk_score, alert_level, language)
    
    # Truncate if needed (though our messages are designed to fit)
    if len(full_message) > max_length:
        return full_message[:max_length-3] + "..."
    
    return full_message


def simulate_alert_delivery(
    village_name: str,
    risk_score: float,
    households: int,
    language: str = "English"
) -> Dict[str, any]:
    """
    Simulate alert delivery across channels.
    
    Args:
        village_name: Name of village
        risk_score: Current risk score
        households: Number of households
        language: Alert language
    
    Returns:
        Dict with delivery simulation results
    """
    alert_level = determine_alert_level(risk_score)
    if alert_level == "No Alert":
        return {"status": "no_alert_needed", "alert_level": "No Alert"}
    
    channels = get_delivery_channels(risk_score)
    sms_message = format_sms_alert(village_name, risk_score, language)
    voice_message = generate_alert_message(village_name, risk_score, alert_level, language)
    
    # Calculate delivery metrics
    mobile_numbers = households * 2  # Estimate 2 phones per household
    
    return {
        "status": "delivered",
        "alert_level": alert_level,
        "channels_used": channels,
        "sms_message": sms_message,
        "voice_message": voice_message,
        "mobile_numbers_reached": mobile_numbers,
        "frequency": get_alert_frequency(risk_score),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "language": language
    }
