# Tests Directory

This folder will contain automated tests for NER-Aegis AI.

## 🧪 Testing Philosophy

For **safety-critical systems**, comprehensive testing is essential:
- ✅ Unit tests for core logic
- ✅ Integration tests for workflows
- ✅ Validation tests against known scenarios
- ✅ Edge case coverage

## 📁 Recommended Structure

```
tests/
├── test_risk_engine.py           # Risk calculation tests
├── test_evacuation_planner.py    # Evacuation logic tests
├── test_alert_engine.py          # Alert generation tests
├── test_integration.py           # End-to-end workflows
├── fixtures/                     # Test data
│   ├── sample_villages.json
│   └── sample_households.json
└── README.md                     # This file
```

## 🎯 Priority Test Cases

### Risk Engine Tests
```python
def test_risk_score_bounds():
    """Risk scores must be between 0-100"""
    pass

def test_confidence_calculation():
    """Confidence bands based on trigger count"""
    pass

def test_factor_contributions():
    """Individual factor contributions sum correctly"""
    pass
```

### Evacuation Planner Tests
```python
def test_household_priority():
    """Priority scores computed correctly"""
    pass

def test_phase_assignment():
    """Households assigned to correct evacuation phases"""
    pass

def test_route_optimization():
    """Alternative routes provided"""
    pass
```

### Alert Engine Tests
```python
def test_alert_level_determination():
    """Correct alert level for risk score"""
    pass

def test_multi_language_messages():
    """All languages generate valid messages"""
    pass

def test_escalation_logic():
    """Alert frequency increases with risk"""
    pass
```

## 🔬 Testing Best Practices

### Safety-Critical Requirements
1. **Conservative failures** - Tests should favor false alarms over missed warnings
2. **Edge cases** - Test boundary conditions thoroughly
3. **Data validation** - All inputs validated
4. **Failure modes** - Test known failure scenarios

### Running Tests
```bash
# Install pytest
pip install pytest pytest-cov

# Run all tests
pytest

# Run with coverage
pytest --cov=logic --cov-report=html

# Run specific test file
pytest tests/test_risk_engine.py

# Run with verbose output
pytest -v
```

## 📊 Coverage Goals

Target coverage:
- **logic/** module: >90%
- Core algorithms: 100%
- Error handling: >80%
- Overall: >85%

## 🚧 Current Status

**Prototype Phase:** Tests to be implemented in production version.

**Why tests matter for safety-critical systems:**
- Lives depend on correct calculations
- Regulatory approval requires test coverage
- Institutional deployment needs validation
- Confidence in system behavior

## 📋 Test Checklist for Production

- [ ] Unit tests for all logic modules
- [ ] Integration tests for workflows
- [ ] Validation against historical data
- [ ] Edge case coverage
- [ ] Performance benchmarks
- [ ] Load testing
- [ ] Security testing
- [ ] Regression test suite
- [ ] Continuous integration configured
- [ ] Test documentation complete

## 🎓 Example Test Structure

```python
# tests/test_risk_engine.py
import pytest
from logic.risk_engine import compute_risk_score, calculate_confidence_level

class TestRiskScoring:
    def test_normal_conditions(self):
        """Test risk score under normal conditions"""
        score = compute_risk_score(
            rainfall=150,
            slope=25,
            soil_moisture=40,
            deforestation=5,
            road_cuts=3
        )
        assert 0 <= score <= 100
        assert score < 50  # Should be low risk
    
    def test_high_risk_conditions(self):
        """Test risk score under high-risk conditions"""
        score = compute_risk_score(
            rainfall=350,
            slope=45,
            soil_moisture=75,
            deforestation=25,
            road_cuts=20
        )
        assert score >= 75  # Should be critical
    
    def test_confidence_with_multiple_triggers(self):
        """High confidence when multiple triggers active"""
        confidence, uncertainty, _ = calculate_confidence_level(
            rainfall=300,
            slope=42,
            soil_moisture=70,
            road_cuts=18,
            deforestation=20
        )
        assert confidence == "High"
        assert uncertainty <= 7

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
```

---

**Remember:** For safety-critical systems, testing is not optional - it's essential.
