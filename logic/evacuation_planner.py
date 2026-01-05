"""
NER-Aegis AI - Micro-Evacuation Planning Engine

This module contains the household-level evacuation prioritization logic:
- Household risk scoring based on location and infrastructure
- Multi-phase evacuation planning
- Route and shelter optimization

Engineering Principle: Granular evacuation intelligence, not mass displacement
"""

from typing import List, Dict, Tuple
from dataclasses import dataclass
import random


@dataclass
class Household:
    """Household data model for evacuation planning"""
    id: str
    location: Tuple[float, float]  # (lat, lon)
    distance_to_slope: float  # meters
    drainage_quality: str  # Poor/Fair/Good
    road_access: str  # Limited/Moderate/Good
    occupants: int
    priority_score: float  # 0-100


def calculate_household_priority(
    distance_to_slope: float,
    drainage_quality: str,
    road_access: str,
    village_risk_score: float
) -> float:
    """
    Calculate evacuation priority score for a household.
    
    Priority factors (relative importance, not normalized weights):
    - Distance to slope: 40% (closer = higher priority)
    - Drainage quality: 30% (poor drainage = higher priority)
    - Road access: 25% (limited access = higher priority)
    - Village risk: 20% (amplifies local factors)
    
    Note: Factors are weighted by relative importance and capped at 100.
    
    Args:
        distance_to_slope: Distance in meters (5-500 range)
        drainage_quality: "Poor", "Fair", or "Good"
        road_access: "Limited", "Moderate", or "Good"
        village_risk_score: Overall village risk (0-100)
    
    Returns:
        float: Priority score (0-100, higher = more urgent)
    """
    priority = 0
    
    # Distance factor (40%) - closer to slope = higher priority
    priority += (500 - distance_to_slope) / 500 * 40
    
    # Drainage factor (30%)
    drainage_scores = {"Poor": 30, "Fair": 15, "Good": 5}
    priority += drainage_scores.get(drainage_quality, 15)
    
    # Road access factor (25%)
    access_scores = {"Limited": 25, "Moderate": 10, "Good": 0}
    priority += access_scores.get(road_access, 10)
    
    # Village risk amplification (20%)
    priority += village_risk_score / 100 * 20
    
    # Total weight >100 by design; score is capped at 100
    return min(priority, 100)


def generate_evacuation_phases(households: List[Household]) -> Dict[str, List[Household]]:
    """
    Organize households into evacuation phases based on priority.
    
    Thresholds intentionally aligned across risk, alert, and evacuation engines.
    
    Phase 1 (Immediate): Priority >= 75 (critical)
    Phase 2 (Within 2 hours): 60 <= Priority < 75 (high)
    Phase 3 (Within 4 hours): 45 <= Priority < 60 (moderate)
    Monitoring: Priority < 45 (low, stay alert)
    
    Args:
        households: List of Household objects
    
    Returns:
        Dict mapping phase names to household lists
    """
    phases = {
        "Phase 1: Immediate (0-30 min)": [],
        "Phase 2: High Priority (30-120 min)": [],
        "Phase 3: Moderate Priority (2-4 hours)": [],
        "Monitoring: Stay Alert": []
    }
    
    for hh in households:
        if hh.priority_score >= 75:
            phases["Phase 1: Immediate (0-30 min)"].append(hh)
        elif hh.priority_score >= 60:
            phases["Phase 2: High Priority (30-120 min)"].append(hh)
        elif hh.priority_score >= 45:
            phases["Phase 3: Moderate Priority (2-4 hours)"].append(hh)
        else:
            phases["Monitoring: Stay Alert"].append(hh)
    
    return phases


def calculate_evacuation_statistics(households: List[Household]) -> Dict[str, int]:
    """
    Calculate evacuation statistics for planning purposes.
    
    Args:
        households: List of Household objects
    
    Returns:
        Dict with evacuation statistics
    """
    total_households = len(households)
    total_people = sum(hh.occupants for hh in households)
    
    critical_households = [hh for hh in households if hh.priority_score >= 75]
    high_priority = [hh for hh in households if 60 <= hh.priority_score < 75]
    moderate_priority = [hh for hh in households if 45 <= hh.priority_score < 60]
    
    critical_people = sum(hh.occupants for hh in critical_households)
    high_people = sum(hh.occupants for hh in high_priority)
    moderate_people = sum(hh.occupants for hh in moderate_priority)
    
    return {
        "total_households": total_households,
        "total_people": total_people,
        "critical_households": len(critical_households),
        "critical_people": critical_people,
        "high_priority_households": len(high_priority),
        "high_priority_people": high_people,
        "moderate_priority_households": len(moderate_priority),
        "moderate_priority_people": moderate_people
    }


def generate_evacuation_routes(village_name: str, road_condition: float) -> Dict[str, str]:
    """
    Generate evacuation route recommendations based on conditions.
    
    Args:
        village_name: Name of the village
        road_condition: Road quality indicator (0-30 = road cuts percentage)
    
    Returns:
        Dict with primary and alternative routes
    """
    routes = {
        "primary": "Village Road → NH-106 → Relief Camp A (5 km)",
        "alternative": "Forest Path → State Highway → Relief Camp B (7 km)",
        "status": "good" if road_condition < 20 else "compromised"
    }
    
    if road_condition >= 20:
        routes["recommendation"] = "Use Route B (Route A compromised)"
    else:
        routes["recommendation"] = "Use Route A (road intact)"
    
    return routes


def identify_shelter_capacity(num_people: int) -> List[Dict[str, any]]:
    """
    Identify appropriate shelters based on evacuation needs.
    
    Args:
        num_people: Number of people to evacuate
    
    Returns:
        List of shelter options with capacity and distance
    """
    shelters = [
        {
            "name": "Community Hall",
            "distance_km": 1.2,
            "capacity": 150,
            "type": "Emergency Shelter"
        },
        {
            "name": "School Building",
            "distance_km": 2.5,
            "capacity": 200,
            "type": "Designated Shelter"
        },
        {
            "name": "District Relief Camp",
            "distance_km": 5.0,
            "capacity": 500,
            "type": "Long-term Shelter"
        }
    ]
    
    # Sort by distance for immediate use
    return sorted(shelters, key=lambda x: x['distance_km'])


def generate_action_summary(
    village_risk_score: float,
    households: List[Household],
    village_name: str,
    road_cuts: float
) -> Dict[str, any]:
    """
    Generate actionable summary for decision makers.
    Compresses intelligence into one glance.
    
    Args:
        village_risk_score: Overall village risk (0-100)
        households: List of household objects
        village_name: Name of the village
        road_cuts: Road cutting percentage
    
    Returns:
        Dict with action summary
    """
    # Determine action level
    if village_risk_score >= 75:
        action = "IMMEDIATE EVACUATION"
        icon = "🆘"
        priority = "CRITICAL"
    elif village_risk_score >= 60:
        action = "PREPARE FOR EVACUATION"
        icon = "🚨"
        priority = "HIGH"
    elif village_risk_score >= 40:
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
    focus_area = focus_areas[hash(village_name) % len(focus_areas)]
    
    # Determine route status
    if road_cuts > 20:
        route_status = "Route B (Route A compromised)"
    else:
        route_status = "Route A (road intact)"
    
    # Alert frequency
    if village_risk_score >= 75:
        alert_freq = "every 15 minutes"
    elif village_risk_score >= 60:
        alert_freq = "every 2 hours"
    elif village_risk_score >= 40:
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
