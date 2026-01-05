"""
NER-Aegis AI - Risk Intelligence Engine

This module contains the core risk assessment algorithms including:
- Multi-factor risk scoring with weighted fusion
- Confidence band calculation based on data quality
- Trigger identification and analysis

Engineering Principle: Separation of intelligence logic from presentation layer
"""

from typing import Dict, Tuple, List
from dataclasses import dataclass


@dataclass
class RiskFactors:
    """Container for risk input factors"""
    rainfall: float  # mm
    slope: float  # degrees
    soil_moisture: float  # percentage
    deforestation: float  # percentage
    road_cuts: float  # percentage


def compute_risk_score(
    rainfall: float, 
    slope: float, 
    soil_moisture: float, 
    deforestation: float, 
    road_cuts: float
) -> float:
    """
    Compute risk score from multiple factors using weighted algorithm.
    This is functional intelligence, not simulation.
    
    Weights based on landslide research:
    - Rainfall: 35% (most critical trigger)
    - Slope: 30% (geological predisposition)
    - Soil moisture: 20% (saturation indicator)
    - Deforestation: 10% (stability loss)
    - Road cuts: 5% (additional destabilization)
    
    Note:
    This function provides relative risk ranking, not probabilistic prediction.
    
    Args:
        rainfall: Rainfall in mm (0-400+ range)
        slope: Slope angle in degrees (0-50 range)
        soil_moisture: Soil moisture percentage (0-100)
        deforestation: Deforestation percentage (0-30 range)
        road_cuts: Road cutting percentage (0-30 range)
    
    Returns:
        float: Composite risk score (0-100)
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


def calculate_risk_contributions(
    rainfall: float,
    slope: float, 
    soil_moisture: float,
    deforestation: float,
    road_cuts: float
) -> Dict[str, float]:
    """
    Calculate how each factor contributes to the risk score.
    Used for explainability and transparency.
    
    Args:
        rainfall: Rainfall in mm
        slope: Slope angle in degrees
        soil_moisture: Soil moisture percentage
        deforestation: Deforestation percentage
        road_cuts: Road cutting percentage
    
    Returns:
        Dict mapping factor names to contribution percentages
    """
    rainfall_contrib = min(rainfall / 400 * 35, 35)
    slope_contrib = min(slope / 50 * 30, 30)
    moisture_contrib = min(soil_moisture / 100 * 20, 20)
    deforest_contrib = min(deforestation / 30 * 10, 10)
    roadcut_contrib = min(road_cuts / 30 * 5, 5)
    
    return {
        "Rainfall surge": rainfall_contrib,
        "Steep slope": slope_contrib,
        "Soil moisture": moisture_contrib,
        "Vegetation loss": deforest_contrib,
        "Road cutting": roadcut_contrib
    }


def calculate_confidence_level(
    rainfall: float,
    slope: float,
    soil_moisture: float,
    road_cuts: float,
    deforestation: float
) -> Tuple[str, int, str]:
    """
    Calculate confidence level for risk score based on data quality and trigger diversity.
    
    Confidence is based on the number of independent triggers active:
    - High confidence (±5-7 pts): 4+ independent triggers
    - Medium confidence (±10 pts): 2-3 triggers
    - Low confidence (±12-15 pts): Single dominant factor
    
    Args:
        rainfall: Rainfall in mm
        slope: Slope angle in degrees
        soil_moisture: Soil moisture percentage
        road_cuts: Road cutting percentage
        deforestation: Deforestation percentage
    
    Returns:
        Tuple of (confidence_level, uncertainty_range, explanation)
    """
    # Count active triggers (threshold-based)
    active_triggers = 0
    trigger_names = []
    
    if rainfall > 250:
        active_triggers += 1
        trigger_names.append("rainfall")
    if slope > 40:
        active_triggers += 1
        trigger_names.append("slope")
    if soil_moisture > 60:
        active_triggers += 1
        trigger_names.append("saturation")
    if road_cuts > 15:
        active_triggers += 1
        trigger_names.append("road-cuts")
    if deforestation > 15:
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
        explanation = f"Strong multi-factor signal ({', '.join(trigger_names[:3])})"
    elif active_triggers == 2:
        confidence = "Medium"
        uncertainty = 10
        explanation = f"Moderate confidence with 2 factors ({', '.join(trigger_names[:3])})"
    elif active_triggers == 1:
        confidence = "Medium-Low"
        uncertainty = 12
        explanation = f"Single dominant factor ({trigger_names[0]})"
    else:
        confidence = "Low"
        uncertainty = 15
        explanation = "Limited trigger activation"
    
    return confidence, uncertainty, explanation


def identify_active_triggers(
    rainfall: float,
    slope: float,
    soil_moisture: float,
    road_cuts: float,
    deforestation: float
) -> List[str]:
    """
    Identify which risk triggers are currently active.
    Used for alert generation and situational awareness.
    
    Args:
        rainfall: Rainfall in mm
        slope: Slope angle in degrees
        soil_moisture: Soil moisture percentage
        road_cuts: Road cutting percentage
        deforestation: Deforestation percentage
    
    Returns:
        List of human-readable trigger descriptions
    """
    triggers = []
    
    if rainfall > 250:
        triggers.append(f"🌧️ Rainfall crossed threshold ({rainfall:.0f} mm)")
    if soil_moisture > 60:
        triggers.append(f"💧 Slope saturation detected ({soil_moisture:.0f}% moisture)")
    if road_cuts > 15:
        triggers.append(f"🛣️ Significant road cutting detected ({road_cuts:.0f}% area affected)")
    if deforestation > 15:
        triggers.append(f"🌲 Vegetation loss critical ({deforestation:.0f}% deforested)")
    if slope > 40:
        triggers.append(f"⛰️ Steep slope instability ({slope:.0f}° average)")
    
    return triggers


def get_risk_category(score: float) -> Tuple[str, str]:
    """
    Categorize risk score into standard risk levels.
    
    Thresholds intentionally aligned across risk, alert, and evacuation engines.
    
    Args:
        score: Risk score (0-100)
    
    Returns:
        Tuple of (category_name, hex_color)
    """
    if score >= 75:
        return "Critical", "#ff4444"
    elif score >= 60:
        return "High", "#ff9800"
    elif score >= 40:
        return "Moderate", "#ffd700"
    else:
        return "Low", "#4caf50"
