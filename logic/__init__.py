"""
NER-Aegis AI - Core Intelligence Module

This package contains the core risk intelligence, evacuation planning,
and alert generation logic, cleanly separated from the presentation layer.

Modules:
- risk_engine: Risk scoring, confidence calculation, trigger identification
- evacuation_planner: Household prioritization, phase planning, route optimization
- alert_engine: Alert level determination, message generation, multi-channel delivery

Engineering Philosophy:
Clean separation of concerns enables:
- Independent testing of intelligence logic
- Reusable algorithms across interfaces (web, mobile, API)
- Clear audit trail of decision logic
- Production-ready architecture

This is not a UI toy - it's a deployable system.
"""

from logic.risk_engine import (
    compute_risk_score,
    calculate_risk_contributions,
    calculate_confidence_level,
    identify_active_triggers,
    get_risk_category
)

from logic.evacuation_planner import (
    calculate_household_priority,
    generate_evacuation_phases,
    calculate_evacuation_statistics,
    generate_evacuation_routes,
    identify_shelter_capacity,
    generate_action_summary
)

from logic.alert_engine import (
    determine_alert_level,
    get_alert_frequency,
    get_delivery_channels,
    generate_alert_message,
    create_alert_escalation_matrix,
    simulate_alert_delivery
)

__version__ = "1.0.0"
__author__ = "NER-Aegis AI Team"

__all__ = [
    # Risk Engine
    'compute_risk_score',
    'calculate_risk_contributions',
    'calculate_confidence_level',
    'identify_active_triggers',
    'get_risk_category',
    
    # Evacuation Planner
    'calculate_household_priority',
    'generate_evacuation_phases',
    'calculate_evacuation_statistics',
    'generate_evacuation_routes',
    'identify_shelter_capacity',
    'generate_action_summary',
    
    # Alert Engine
    'determine_alert_level',
    'get_alert_frequency',
    'get_delivery_channels',
    'generate_alert_message',
    'create_alert_escalation_matrix',
    'simulate_alert_delivery'
]
