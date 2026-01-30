# Changelog

All notable changes to NER-Aegis AI will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-01-27

### 🎯 Initial Release - Competition Version

#### Added
- **Core Features (5/5 Must-Have)**
  - Village-level risk intelligence dashboard with interactive map
  - Explainable risk breakdown with factor contributions
  - Micro-evacuation engine with household prioritization
  - Multi-language alert system (English, Hindi, Khasi)
  - Clear scope framing ("risk intelligence, not prediction")

- **High-Impact Add-Ons (4/4)**
  - Time-based risk trend analysis (7-14 days)
  - Real-time trigger identification panel
  - Offline-first design with 7-day caching
  - Dual user interfaces (Officer Mode / Citizen Mode)

- **Advanced Intelligence Features**
  - Computed risk scores with weighted fusion algorithm
  - Confidence bands based on trigger diversity (±5 to ±15 points)
  - Action summary cards for quick decision-making
  - Progressive alert escalation (Advisory → Warning → Evacuate)

- **Engineering Maturity**
  - Clean `logic/` folder structure separating business logic from UI
  - Comprehensive documentation (6 failure modes, assumptions, constraints)
  - Glassmorphism UI with government-appropriate aesthetic
  - Production-ready architecture (microservices-ready)

- **Documentation**
  - Complete README with visual structure
  - QUICKSTART guide for 3-minute setup
  - TROUBLESHOOTING guide for common issues
  - Comprehensive IMPROVEMENTS documentation
  - FEATURES_CHECKLIST with 19/19 features

#### Risk Scoring Algorithm
```python
Risk = Rainfall(35%) + Slope(30%) + Moisture(20%) + 
       Deforestation(10%) + RoadCuts(5%)
```

#### Evacuation Priority Algorithm
```python
Priority = Distance(40%) + Drainage(30%) + 
           Access(25%) + VillageRisk(20%)
```

#### Technical Stack
- Framework: Streamlit
- Data: Pandas, NumPy
- Visualization: Plotly, Folium
- Maps: OpenStreetMap
- Backend: Custom Python modules

#### Known Limitations
- Prototype data (not real-time satellite feeds)
- Optimized for hours-to-days warning (not minutes)
- Requires periodic calibration with ground truth
- 10 demo villages (production would scale to 1000+)

---

## [Unreleased]

### Planned for v2.0 (Post-Hackathon)
- Integration with official data sources (IMD, ISRO)
- Longitudinal validation with historical datasets
- Policy-led expansion to additional districts
- Real-time satellite data integration
- Enhanced mobile responsiveness
- API for third-party integration

---

## Version History

- **v1.0.0** (2026-01-27) - Initial competition release
- **v0.9.0** (2026-01-26) - Final polish and UI improvements
- **v0.8.0** (2026-01-25) - Logic module separation
- **v0.7.0** (2026-01-24) - Micro-evacuation engine
- **v0.6.0** (2026-01-23) - Multi-language alerts
- **v0.5.0** (2026-01-22) - Confidence bands
- **v0.4.0** (2026-01-21) - Explainable risk breakdown
- **v0.3.0** (2026-01-20) - Interactive map dashboard
- **v0.2.0** (2026-01-19) - Risk scoring algorithm
- **v0.1.0** (2026-01-18) - Initial prototype

---

## Contribution Guidelines

See [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.
