#!/usr/bin/env python3
"""
NER-Aegis AI - Compatibility Test Suite
Tests that all components work together correctly
"""

import sys
import os

def test_imports():
    """Test that all required modules can be imported"""
    print("Testing imports...")
    try:
        import streamlit
        print("  ✅ streamlit imported")
        
        import pandas
        print("  ✅ pandas imported")
        
        import numpy
        print("  ✅ numpy imported")
        
        import plotly
        print("  ✅ plotly imported")
        
        import folium
        print("  ✅ folium imported")
        
        from logic import risk_engine, evacuation_planner, alert_engine
        print("  ✅ logic modules imported")
        
        return True
    except ImportError as e:
        print(f"  ❌ Import error: {e}")
        return False

def test_risk_engine():
    """Test risk engine functions"""
    print("\nTesting risk_engine module...")
    try:
        from logic.risk_engine import (
            compute_risk_score,
            calculate_confidence_level,
            identify_active_triggers,
            get_risk_category,
            calculate_risk_contributions
        )
        
        # Test compute_risk_score
        score = compute_risk_score(300, 40, 60, 15, 10)
        assert 0 <= score <= 100, f"Invalid score: {score}"
        print(f"  ✅ compute_risk_score: {score:.1f}")
        
        # Test confidence calculation
        conf, unc, exp = calculate_confidence_level(300, 40, 60, 15, 10)
        assert conf in ['High', 'High-Medium', 'Medium', 'Medium-Low', 'Low']
        assert 0 <= unc <= 20
        print(f"  ✅ calculate_confidence_level: {conf} (±{unc})")
        
        # Test risk category
        category, color = get_risk_category(score)
        assert category in ['Low', 'Moderate', 'High', 'Critical']
        print(f"  ✅ get_risk_category: {category}")
        
        # Test contributions
        contributions = calculate_risk_contributions(300, 40, 60, 15, 10)
        assert isinstance(contributions, dict)
        print(f"  ✅ calculate_risk_contributions: {len(contributions)} factors")
        
        # Test triggers
        triggers = identify_active_triggers(300, 40, 60, 15, 10)
        assert isinstance(triggers, list)
        print(f"  ✅ identify_active_triggers: {len(triggers)} triggers")
        
        return True
    except Exception as e:
        print(f"  ❌ Risk engine error: {e}")
        return False

def test_evacuation_planner():
    """Test evacuation planner functions"""
    print("\nTesting evacuation_planner module...")
    try:
        from logic.evacuation_planner import (
            calculate_household_priority,
            generate_action_summary
        )
        
        # Test household priority
        priority = calculate_household_priority(50, 'Poor', 'Limited', 70)
        assert 0 <= priority <= 100, f"Invalid priority: {priority}"
        print(f"  ✅ calculate_household_priority: {priority:.1f}")
        
        # Test different drainage qualities
        for drainage in ['Poor', 'Fair', 'Good']:
            p = calculate_household_priority(100, drainage, 'Moderate', 50)
            assert 0 <= p <= 100
        print(f"  ✅ Drainage quality variations work")
        
        # Test different road access
        for access in ['Limited', 'Moderate', 'Good']:
            p = calculate_household_priority(100, 'Fair', access, 50)
            assert 0 <= p <= 100
        print(f"  ✅ Road access variations work")
        
        # Test action summary with mock data
        class MockHousehold:
            def __init__(self, priority_score):
                self.priority_score = priority_score
        
        households = [MockHousehold(p) for p in [90, 85, 75, 70, 60, 50, 40, 30]]
        summary = generate_action_summary(75, households, "Test Village", 15)
        
        assert 'action' in summary
        assert 'households_evacuate' in summary
        print(f"  ✅ generate_action_summary: {summary['action']}")
        
        return True
    except Exception as e:
        print(f"  ❌ Evacuation planner error: {e}")
        return False

def test_alert_engine():
    """Test alert engine functions"""
    print("\nTesting alert_engine module...")
    try:
        from logic.alert_engine import (
            determine_alert_level,
            get_alert_frequency,
            get_delivery_channels,
            generate_alert_message
        )
        
        # Test alert levels
        test_scores = [30, 50, 65, 80]
        expected_levels = ['No Alert', 'Advisory', 'Warning', 'Evacuate']
        
        for score, expected in zip(test_scores, expected_levels):
            level = determine_alert_level(score)
            assert level == expected, f"Score {score}: expected {expected}, got {level}"
        print(f"  ✅ determine_alert_level: all thresholds correct")
        
        # Test alert frequency
        freq = get_alert_frequency(80)
        assert isinstance(freq, str)
        print(f"  ✅ get_alert_frequency: {freq}")
        
        # Test delivery channels
        channels = get_delivery_channels(80)
        assert isinstance(channels, list)
        assert len(channels) > 0
        print(f"  ✅ get_delivery_channels: {len(channels)} channels")
        
        # Test multi-language messages
        for lang in ['English', 'Hindi', 'Khasi']:
            msg = generate_alert_message("Test Village", 75, "Evacuate", lang)
            assert len(msg) > 0
            assert "Test Village" in msg
        print(f"  ✅ generate_alert_message: 3 languages work")
        
        return True
    except Exception as e:
        print(f"  ❌ Alert engine error: {e}")
        return False

def test_integration():
    """Test that modules work together"""
    print("\nTesting module integration...")
    try:
        from logic.risk_engine import compute_risk_score, calculate_confidence_level
        from logic.evacuation_planner import calculate_household_priority
        from logic.alert_engine import determine_alert_level, generate_alert_message
        
        # Simulate a complete workflow
        # 1. Calculate risk
        risk_score = compute_risk_score(320, 42, 65, 20, 18)
        print(f"  ✅ Step 1 - Risk calculated: {risk_score:.1f}")
        
        # 2. Get confidence
        confidence, uncertainty, explanation = calculate_confidence_level(320, 42, 65, 18, 20)
        print(f"  ✅ Step 2 - Confidence: {confidence} (±{uncertainty})")
        
        # 3. Determine alert level
        alert_level = determine_alert_level(risk_score)
        print(f"  ✅ Step 3 - Alert level: {alert_level}")
        
        # 4. Calculate household priorities
        households_priorities = []
        for distance in [30, 50, 100, 150]:
            priority = calculate_household_priority(distance, 'Poor', 'Limited', risk_score)
            households_priorities.append(priority)
        print(f"  ✅ Step 4 - {len(households_priorities)} households prioritized")
        
        # 5. Generate alert message
        if alert_level != "No Alert":
            message = generate_alert_message("Test Village", risk_score, alert_level, "English")
            assert len(message) > 0
            print(f"  ✅ Step 5 - Alert generated")
        else:
            print(f"  ✅ Step 5 - No alert needed (correct)")
        
        return True
    except Exception as e:
        print(f"  ❌ Integration error: {e}")
        return False

def test_file_structure():
    """Test that all required files exist"""
    print("\nTesting file structure...")
    required_files = [
        'app.py',
        'requirements.txt',
        'setup.sh',
        'README.md',
        'LICENSE',
        'CONTRIBUTING.md',
        'CODE_OF_CONDUCT.md',
        'SECURITY.md',
        'CHANGELOG.md',
        '.gitignore',
        'logic/__init__.py',
        'logic/risk_engine.py',
        'logic/evacuation_planner.py',
        'logic/alert_engine.py',
        'logic/README.md',
    ]
    
    all_exist = True
    for file in required_files:
        if os.path.exists(file):
            print(f"  ✅ {file}")
        else:
            print(f"  ❌ {file} MISSING")
            all_exist = False
    
    return all_exist

def main():
    """Run all compatibility tests"""
    print("╔══════════════════════════════════════════════════════════╗")
    print("║                                                          ║")
    print("║         NER-Aegis AI - Compatibility Test Suite         ║")
    print("║                                                          ║")
    print("╚══════════════════════════════════════════════════════════╝")
    print()
    
    results = []
    
    # Run all tests
    results.append(("File Structure", test_file_structure()))
    results.append(("Imports", test_imports()))
    results.append(("Risk Engine", test_risk_engine()))
    results.append(("Evacuation Planner", test_evacuation_planner()))
    results.append(("Alert Engine", test_alert_engine()))
    results.append(("Integration", test_integration()))
    
    # Summary
    print("\n" + "="*60)
    print("COMPATIBILITY TEST SUMMARY")
    print("="*60)
    
    all_passed = True
    for test_name, passed in results:
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{test_name:.<40} {status}")
        if not passed:
            all_passed = False
    
    print("="*60)
    
    if all_passed:
        print("\n🎉 ALL COMPATIBILITY TESTS PASSED!")
        print("✅ All files are compatible with each other")
        print("✅ System is ready for deployment")
        return 0
    else:
        print("\n❌ SOME TESTS FAILED")
        print("⚠️  Please fix the issues above")
        return 1

if __name__ == "__main__":
    sys.exit(main())
