# 🚀 NER-Aegis AI - One-Page Quick Reference

**Get up and running in 3 minutes!**

---

## ⚡ Super Quick Start

### Copy-Paste This:
```bash
git clone https://github.com/your-org/ner-aegis-ai.git
cd ner-aegis-ai
bash setup.sh
```

**Done!** App opens automatically at `http://localhost:8501` 🎉

---

## 🎯 Manual Installation (Alternative)

```bash
# Step 1: Install dependencies
pip install -r requirements.txt

# Step 2: Run app
streamlit run app.py
```

---

## 📱 First Demo (5 Minutes)

### Officer Mode Demo Flow
```
1. Select "Disaster Officer" → Sidebar
2. View Dashboard → See 10 villages
3. Click "Cherrapunji" → High-risk example
4. See Risk Score: 72 (±7) → With confidence band
5. Check "Micro-Evacuation" tab → 14 households prioritized
6. Preview "Alerts" tab → Multi-language messages
```

### Citizen Mode Demo Flow
```
1. Select "Citizen View" → Sidebar
2. Choose "Cherrapunji" → Dropdown
3. See: "🚨 WARNING" → Clear risk display
4. Read Instructions → What to do now
5. Check Contacts → Emergency numbers
```

---

## 🎨 Visual Guide

### Main Interface

```
┌─────────────────────────────────────────────────────┐
│  Sidebar              │  Main Content Area          │
│ ┌─────────────────┐  │                             │
│ │ User Mode:      │  │  📊 SYSTEM OVERVIEW         │
│ │ ○ Officer       │  │  ┌────┬────┬────┬────┐     │
│ │ ○ Citizen       │  │  │ 10 │ 2  │3.2K│62.5│     │
│ │                 │  │  └────┴────┴────┴────┘     │
│ │ Village Filter  │  │                             │
│ │ [Dropdown]      │  │  🗺️  INTERACTIVE MAP        │
│ │                 │  │  [Click villages]           │
│ │ Settings        │  │                             │
│ └─────────────────┘  │  📈 RISK DISTRIBUTION       │
│                      │  [Charts & Graphs]          │
└─────────────────────────────────────────────────────┘
```

### Village Detail View

```
┌─────────────────────────────────────────────────────┐
│  🏔️ Cherrapunji - Village Analysis                │
├─────────────────────────────────────────────────────┤
│  📊 Risk Score: 72 (High) ±7 points                │
│  🎯 Confidence: High-Medium (rainfall, slope)      │
├─────────────────────────────────────────────────────┤
│  Tabs: │Overview│Evacuation│Trends│Alerts│        │
├─────────────────────────────────────────────────────┤
│                                                     │
│  ⚡ WHAT TRIGGERED THIS ALERT:                     │
│  • 🌧️ Rainfall: 320mm (threshold: 250mm)          │
│  • ⛰️ Slope: 42° (threshold: 40°)                  │
│                                                     │
│  🚨 ACTION SUMMARY:                                │
│  • Evacuate: 14 households (8 critical)            │
│  • Route: Use Route A (intact)                     │
│  • Timeframe: Next 6 hours                         │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

## 🔧 Troubleshooting

### Problem: App won't start
```bash
# Solution 1: Check Python version
python --version  # Need 3.8+

# Solution 2: Reinstall dependencies
pip install -r requirements.txt --upgrade

# Solution 3: Use python -m
python -m streamlit run app.py
```

### Problem: Port already in use
```bash
# Streamlit auto-selects new port
# Check terminal for: "You can now view your app in your browser."
# Use the URL shown (e.g., http://localhost:8502)
```

### Problem: Import errors
```bash
# Ensure you're in project directory
cd ner-aegis-ai
pwd  # Should end with /ner-aegis-ai

# Then run again
streamlit run app.py
```

### Problem: No villages showing
```bash
# This is normal - click the map or use dropdown
# Villages load on interaction
```

---

## 📊 Key Features Checklist

Use this to verify everything works:

- [ ] **Dashboard loads** - See 4 metric cards at top
- [ ] **Map displays** - 10 villages visible on map
- [ ] **Village clickable** - Click opens detail view
- [ ] **Risk score visible** - Shows number + confidence band
- [ ] **Explainable factors** - See 5 contributing factors
- [ ] **Evacuation tab** - Shows household priority list
- [ ] **Trends chart** - 7-day risk trend graph
- [ ] **Alerts preview** - SMS/Voice message samples
- [ ] **Citizen mode** - Switch sidebar, see simple view
- [ ] **Multi-language** - Change language in alerts

**All checked?** ✅ System fully functional!

---

## 🎬 5-Minute Demo Script

**For judges or presentations:**

```
[0:00-0:30] Introduction
"NER-Aegis AI provides hours-to-days early warning for Northeast 
India micro-landslides with village-level risk intelligence and 
household-level evacuation planning."

[0:30-1:30] Dashboard Overview
"Here's our system overview - 10 villages, 2 critical, 3,200 people 
monitored. The interactive map shows real-time risk levels."

[1:30-3:00] Village Deep-Dive (Cherrapunji)
"Let's look at Cherrapunji - risk score 72, high confidence. 
Notice the explainable breakdown: rainfall 35%, slope 30%. 
Our micro-evacuation tab prioritizes 14 specific households 
for immediate evacuation - this is our killer differentiator."

[3:00-4:00] Alerts & Features
"Multi-language alerts - English, Hindi, Khasi. Progressive 
escalation: advisory → warning → evacuate. See the confidence 
bands - we don't claim false precision."

[4:00-5:00] Citizen View & Closing
"Simplified citizen interface - clear instructions, emergency 
contacts. This is decision support, not prediction. Final 
decisions rest with District Disaster Officers. Built for 
real deployment with offline capability and failure mode 
documentation."
```

---

## 🆘 Emergency Commands

**Stop the app:**
```
Press Ctrl+C in terminal
```

**Restart the app:**
```bash
streamlit run app.py
```

**Clear cache and restart:**
```bash
streamlit cache clear
streamlit run app.py
```

**Check if streamlit is installed:**
```bash
pip show streamlit
```

**Force reinstall everything:**
```bash
pip uninstall -y -r requirements.txt
pip install -r requirements.txt
```

---

## 📞 Quick Links

| Resource | Link |
|----------|------|
| Full Documentation | [README.md](README.md) |
| Detailed Setup | [QUICKSTART.md](QUICKSTART.md) |
| Troubleshooting | [TROUBLESHOOTING.md](TROUBLESHOOTING.md) |
| Features List | [FEATURES_CHECKLIST.md](FEATURES_CHECKLIST.md) |
| Contributing | [CONTRIBUTING.md](CONTRIBUTING.md) |

---

## ✅ Success Checklist

**Before demo/submission:**

- [ ] App runs without errors
- [ ] All 10 villages load
- [ ] Risk scores display with confidence bands
- [ ] Evacuation priorities show households
- [ ] Alerts generate in all 3 languages
- [ ] Citizen mode works
- [ ] No console errors
- [ ] Tested on clean Python environment

---

## 💡 Pro Tips

**For Best Demo:**
1. ✅ Start with Officer mode (shows full capability)
2. ✅ Use Cherrapunji or Shillong Peak (high-risk examples)
3. ✅ Emphasize household-level evacuation (unique feature)
4. ✅ Show confidence bands (responsible AI)
5. ✅ Switch to Citizen mode (dual stakeholder awareness)

**For Judges:**
1. ✅ Mention "hours-to-days warning" (scope clarity)
2. ✅ Highlight "decision support, not prediction" (honesty)
3. ✅ Point out `logic/` folder (engineering maturity)
4. ✅ Show failure modes in docs (safety awareness)
5. ✅ Reference decision authority (policy awareness)

---

**Need more help?** 

→ See full [README.md](README.md) for comprehensive documentation  
→ Check [TROUBLESHOOTING.md](TROUBLESHOOTING.md) for detailed solutions  
→ Review [QUICKSTART.md](QUICKSTART.md) for step-by-step guide

---

**Last Updated:** January 29, 2026  
**Version:** 1.0  
**Status:** ✅ Production Ready
