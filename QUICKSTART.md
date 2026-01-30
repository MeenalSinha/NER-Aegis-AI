# 🚀 NER-Aegis AI - Quick Start Guide

## ⚡ 3-Minute Setup

### Step 1: Install Dependencies (30 seconds)
```bash
pip install -r requirements.txt
```

### Step 2: Run Application (10 seconds)
```bash
streamlit run app.py
```

### Step 3: Open Browser (Automatic)
The application will automatically open at `http://localhost:8501`

---

## 🎯 Demo Flow for Judges/Reviewers

### Part 1: Overview Dashboard (2 minutes)

1. **Start in "Disaster Officer" mode**
2. **View the Overview page** to see:
   - ✅ All 10 villages on interactive map
   - ✅ Risk heatmap with color coding
   - ✅ Key system metrics
   - ✅ High-risk village list
   - ✅ Active alerts
   - ✅ Risk distribution charts

### Part 2: Village Deep-Dive (3 minutes)

1. **Select "Cherrapunji"** (High Risk - 72) from dropdown
2. **Show these KEY features:**
   
   #### 🎯 Risk Score with Confidence Band ⭐ NEW
   - Risk Score: 72 (High)
   - **Confidence: High-Medium (±7 points)**
   - Shows epistemic humility
   - Based on trigger diversity
   
   #### ⚡ Action Summary Card ⭐ NEW
   - **One-glance intelligence**
   - Recommended action: Next 6 Hours
   - Households to evacuate: 14 (8 critical)
   - Focus area: eastern slope
   - Route: Route A (road intact)
   - Alert frequency: every 15 minutes
   
   #### 🔍 Explainable Risk Breakdown
   - **Computed dynamically** (not hardcoded)
   - Rainfall surge: +32%
   - Steep slope: +26%
   - Road cutting: +12%
   - Vegetation loss: +8%
   
   #### 📊 Risk Trend
   - 7-day trend graph
   - Shows risk increasing/decreasing
   - Quantified change
   
   #### ⚡ Alert Triggers
   - Specific reasons for current alert level
   - "Rainfall crossed threshold"
   - "Slope saturation detected"

### Part 3: Micro-Evacuation (2 minutes) ⭐ KILLER FEATURE

1. **Scroll to Evacuation Planning section**
2. **Demonstrate:**
   - ✅ Priority-ranked household list (top 10)
   - ✅ Each household shows:
     - Distance to slope
     - Drainage quality
     - Road access
     - Number of occupants
   - ✅ Evacuation summary:
     - How many households
     - How many people
     - Phase 1 vs Phase 2
   - ✅ Evacuation routes and shelters
   - ✅ Timeline chart

### Part 4: Alert Simulation (1 minute)

1. **Show SMS Alert Preview**
   - Real message text
   - Delivery count
2. **Show Voice Alert**
   - Change language to Hindi or Khasi
   - Show localized message
3. **Show Alert Escalation Matrix**
   - Different levels based on risk

### Part 5: Citizen Mode (1 minute)

1. **Switch to "Citizen View"** in sidebar
2. **Select a village**
3. **Show simplified interface:**
   - Large risk score display
   - Simple instructions (what to do)
   - Emergency contacts
   - Risk trend
   - No overwhelming data

---

## 🎬 Script for Live Demo

### Opening (30 seconds)
> "NER-Aegis AI solves a critical problem: micro-landslides in Northeast India that don't trigger national alerts but still kill people. Current systems are coarse and district-level. We provide hyperlocal, village-level risk intelligence with household-specific evacuation plans."

### Feature Highlight 1: Hyperlocal Intelligence (30 seconds)
> "Here's our interactive dashboard showing 10 Northeast villages. Each dot represents a village, color-coded by risk level. Notice we're operating at village-level, not district-level. Click any village for detailed analysis."

### Feature Highlight 2: Computed Intelligence + Confidence (1 minute) ⭐ NEW
> "Our risk scores aren't hardcoded—they're computed dynamically from multiple factors using a weighted algorithm. But here's what sets us apart: we show confidence bands. This score of 72 has a confidence of ±7 points based on trigger diversity. This epistemic humility is research-grade thinking—we acknowledge uncertainty rather than claiming false precision."

### Feature Highlight 3: Action Summary Card (45 seconds) ⭐ NEW  
> "Decision-makers need intelligence at a glance. This Action Summary Card compresses everything into one view: evacuate 14 households in the next 6 hours, focus on eastern slope, use Route A, repeat alerts every 15 minutes. Judges often skim—this instant summary is gold."

### Feature Highlight 4: Explainability (30 seconds)
> "This is our explainable risk breakdown. We don't just say 'High Risk' - we show exactly WHY. Rainfall contributes 32%, steep slopes 26%, and so on. This transparency builds trust with officials and communities. We also show what triggered the alert - rainfall crossed threshold, slope saturation detected."

### Feature Highlight 5: Micro-Evacuation (1 minute) ⭐⭐⭐
> "This is our killer differentiator: micro-evacuation planning. Almost no team goes this deep. We identify specific households that need to evacuate, prioritize them based on distance to slope, drainage quality, and road access. We even show which households to evacuate first, suggest routes, and identify shelters. This isn't just 'evacuate the village' - it's 'evacuate these 15 households in this order to these specific locations.'"

### Feature Highlight 6: Not Prediction (20 seconds)
> "Critically, we frame this as risk intelligence, NOT landslide prediction. This disclaimer appears everywhere in the app. We're not making false promises - we're providing probabilistic risk assessment to support decision-making."

### Feature Highlight 7: Last-Mile Delivery (30 seconds)
> "We simulate last-mile alert delivery with SMS previews and voice alerts in local languages - English, Hindi, and Khasi. Alerts escalate from Advisory to Warning to Evacuate based on risk levels."

### Feature Highlight 8: Dual Interface (30 seconds)
> "We have two modes: Disaster Officer mode with full analytics, and Citizen mode with simplified, actionable information. Different stakeholders need different interfaces."

### Closing (30 seconds)
> "In summary: computed risk intelligence with confidence bands, one-glance action summaries, hyperlocal village-level intelligence, explainable AI, household-specific evacuation plans, multi-language alerts, and offline-first design. This shows epistemic humility and research-grade thinking while addressing a real gap in disaster management with features that almost no other teams implement."

---

## 🏆 Key Talking Points

### Problem Validation
- Northeast India has frequent micro-landslides
- Current systems are district-level, too coarse
- Alerts come too late or not at all
- No household-level evacuation guidance

### Innovation
1. **Hyperlocal**: Village and household level (not district)
2. **Explainable**: Shows WHY risk is high
3. **Actionable**: Specific households, routes, shelters
4. **Culturally Aware**: Local language support
5. **Realistic**: Offline-first for connectivity issues

### Technical Sophistication
- Multi-factor risk fusion
- Priority optimization algorithm
- Temporal trend analysis
- Alert escalation logic
- Dual user interfaces

---

## 🎨 Visual Impact Tips

### When Demoing
1. **Start with the map** - Immediate visual impact
2. **Use a high-risk village** - Shows all features
3. **Hover over data points** - Show interactivity
4. **Switch languages** - Demonstrate localization
5. **Toggle between modes** - Show stakeholder awareness

### Color Psychology
- 🔴 Red = Urgent action required
- 🟠 Orange = Warning, prepare
- 🟡 Yellow = Stay alert
- 🟢 Green = Normal activities

---

## 📊 Key Metrics to Highlight

- **10 villages** monitored
- **Village-level** precision (not district)
- **Household-level** evacuation planning
- **3 languages** supported
- **4 risk categories** (Low/Moderate/High/Critical)
- **5 risk factors** explained
- **7-14 day** trend analysis
- **2 user modes** (Officer/Citizen)

---

## ❓ Anticipated Questions & Answers

### Q: How is this different from existing systems?
**A:** Existing systems operate at district level and just send generic alerts. We provide village-level risk intelligence, explain WHY risk is high, and tell you WHICH specific households need to evacuate first with specific routes and shelters.

### Q: Can this actually predict landslides?
**A:** No, and we're very clear about that. We provide risk intelligence based on multiple factors. The system helps decision-makers assess risk, not predict exact landslide occurrences.

### Q: What about data sources?
**A:** In production, this would connect to satellite imagery APIs, weather stations, soil sensors, and ground reports. This demo uses representative data patterns to show the full system functionality.

### Q: How does it work offline?
**A:** The system caches last 7 days of data, pre-downloads maps, and queues alerts. When connectivity returns, it syncs new data and sends pending alerts.

### Q: Why household-level detail?
**A:** Mass evacuations are disruptive and expensive. Targeted micro-evacuations of 10-30 highest-risk households are more practical and save lives without unnecessary displacement.

---

## 🎯 Success Criteria

You've succeeded in the demo if judges say:
- ✅ "I've never seen household-level evacuation planning before"
- ✅ "The explainability is really clear"
- ✅ "This addresses a real gap"
- ✅ "The dual interface shows stakeholder understanding"
- ✅ "The 'not prediction' framing is mature"

---

## 🔥 Power Tips

1. **Start with high-risk village** - Shows all features active
2. **Emphasize micro-evacuation** - Your differentiator
3. **Show, don't tell** - Click through features live
4. **Be confident about limitations** - "Risk intelligence, not prediction"
5. **Highlight offline capability** - Shows deployment realism

---

**Good luck! You've got a winner here. 🚀**
