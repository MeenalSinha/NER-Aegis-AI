# 🔧 NER-Aegis AI - Troubleshooting Guide

## Common Issues and Solutions

### Issue 1: Installation Errors

#### Problem: `pip install` fails
**Solution:**
```bash
# Try upgrading pip first
python3 -m pip install --upgrade pip

# Then install requirements
pip3 install -r requirements.txt

# If still failing, install packages individually
pip3 install streamlit
pip3 install pandas
pip3 install numpy
pip3 install plotly
pip3 install folium
pip3 install streamlit-folium
```

#### Problem: Permission denied
**Solution:**
```bash
# Use --user flag
pip3 install -r requirements.txt --user

# Or use sudo (Linux/Mac)
sudo pip3 install -r requirements.txt
```

---

### Issue 2: Application Won't Start

#### Problem: `streamlit: command not found`
**Solution:**
```bash
# Find where streamlit was installed
python3 -m streamlit run app.py

# Or add to PATH (Linux/Mac)
export PATH="$HOME/.local/bin:$PATH"

# Then run normally
streamlit run app.py
```

#### Problem: Port already in use
**Solution:**
```bash
# Run on different port
streamlit run app.py --server.port 8502

# Or kill existing process (Linux/Mac)
lsof -ti:8501 | xargs kill -9

# Then run normally
streamlit run app.py
```

---

### Issue 3: Map Not Displaying

#### Problem: Folium map shows blank
**Solution:**
1. Check internet connection (OpenStreetMap tiles need internet)
2. Try refreshing the page (Ctrl+R or Cmd+R)
3. Check browser console for errors (F12)
4. Ensure folium and streamlit-folium are installed:
   ```bash
   pip3 install folium streamlit-folium --upgrade
   ```

---

### Issue 4: Charts Not Rendering

#### Problem: Plotly charts not showing
**Solution:**
```bash
# Upgrade plotly
pip3 install plotly --upgrade

# Clear Streamlit cache
streamlit cache clear

# Restart application
```

---

### Issue 5: Slow Performance

#### Problem: Application is slow
**Solution:**
1. **Check Python version** (3.8+ recommended)
   ```bash
   python3 --version
   ```

2. **Clear cache**
   ```bash
   streamlit cache clear
   ```

3. **Reduce data points** (in app.py, adjust):
   ```python
   # Change from 20 to 10 households
   households = generate_households(village, 10)
   ```

4. **Close other applications**
   - Free up RAM
   - Close unnecessary browser tabs

---

### Issue 6: Styling Issues

#### Problem: Custom CSS not applying
**Solution:**
1. **Force refresh** browser (Ctrl+Shift+R or Cmd+Shift+R)
2. **Clear browser cache**
3. **Check Streamlit version**:
   ```bash
   pip3 install streamlit==1.31.0
   ```

---

### Issue 7: Data Not Loading

#### Problem: Villages not appearing
**Solution:**
1. **Check function calls** in app.py
2. **Verify data generation**:
   ```python
   # In Python console
   from app import generate_ne_villages
   villages = generate_ne_villages()
   print(len(villages))  # Should print 10
   ```

3. **Restart application** completely

---

### Issue 8: Browser Doesn't Open Automatically

#### Problem: App runs but browser doesn't open
**Solution:**
1. **Manually open browser** and go to:
   ```
   http://localhost:8501
   ```

2. **Check if port is blocked**:
   ```bash
   # Linux/Mac
   netstat -an | grep 8501
   
   # Windows
   netstat -an | findstr 8501
   ```

3. **Try different browser** (Chrome, Firefox, Safari)

---

### Issue 9: Module Import Errors

#### Problem: `ModuleNotFoundError: No module named 'streamlit'`
**Solution:**
```bash
# Ensure you're using the correct Python
which python3

# Install in the right environment
python3 -m pip install -r requirements.txt

# Or create virtual environment
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows

pip install -r requirements.txt
streamlit run app.py
```

---

### Issue 10: Sidebar Not Showing

#### Problem: Sidebar collapsed or missing
**Solution:**
1. **Click hamburger menu** (☰) in top-left corner
2. **Check screen size** (may auto-collapse on small screens)
3. **Try full-screen mode** (F11)
4. **Refresh page**

---

## Platform-Specific Issues

### Windows

#### Problem: `bash: streamlit: command not found`
**Solution:**
```cmd
# Use full path
python -m streamlit run app.py

# Or find Scripts directory
where streamlit

# Add to PATH environment variable
```

#### Problem: Setup.sh won't run
**Solution:**
```cmd
# Use Git Bash or WSL
# Or run commands manually:
pip install -r requirements.txt
python -m streamlit run app.py
```

### macOS

#### Problem: Permission issues
**Solution:**
```bash
# Give execute permission
chmod +x setup.sh

# Run setup
./setup.sh

# Or use sudo for pip
sudo pip3 install -r requirements.txt
```

### Linux

#### Problem: Python version too old
**Solution:**
```bash
# Install Python 3.8+
sudo apt update
sudo apt install python3.8 python3-pip

# Use specific version
python3.8 -m pip install -r requirements.txt
python3.8 -m streamlit run app.py
```

---

## Performance Optimization

### For Slow Computers

1. **Reduce trend days**: Change slider to 3 days instead of 7
2. **Limit households**: Show top 5 instead of top 10
3. **Simplify charts**: Remove some visualizations
4. **Use Citizen Mode**: Less data-intensive

### For Large Deployments

1. **Use caching**: Add `@st.cache_data` decorators
2. **Database backend**: Replace in-memory data
3. **CDN for maps**: Host tiles locally
4. **Load balancing**: Multiple Streamlit instances

---

## Data Issues

### Problem: Unrealistic risk scores
**Solution:**
This is a demo with simulated data. In production:
1. Connect to real satellite APIs
2. Use actual weather station data
3. Integrate soil sensor readings
4. Validate with historical events

### Problem: Static data
**Solution:**
The demo uses static simulated data. To make it dynamic:
1. Add real-time data feeds
2. Implement data refresh intervals
3. Connect to live APIs
4. Add database integration

---

## Browser Compatibility

### Recommended Browsers
- ✅ Chrome/Chromium (80+)
- ✅ Firefox (75+)
- ✅ Safari (13+)
- ✅ Edge (80+)

### Known Issues
- ❌ Internet Explorer (not supported)
- ⚠️ Older mobile browsers (may have layout issues)

---

## Debug Mode

### Enable Debug Output

Add to app.py:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

Run with verbose output:
```bash
streamlit run app.py --logger.level=debug
```

---

## Getting Help

### If Nothing Works

1. **Check Python version**: Must be 3.8+
   ```bash
   python3 --version
   ```

2. **Create fresh virtual environment**:
   ```bash
   python3 -m venv fresh_env
   source fresh_env/bin/activate
   pip install -r requirements.txt
   streamlit run app.py
   ```

3. **Check Streamlit documentation**: https://docs.streamlit.io

4. **Review error messages**: Copy full error to search engine

---

## Quick Fixes Summary

| Issue | Quick Fix |
|-------|-----------|
| Won't install | `python3 -m pip install --upgrade pip` |
| Won't start | `python3 -m streamlit run app.py` |
| Map blank | Check internet, refresh browser |
| Slow | Reduce data points, close tabs |
| Port busy | `streamlit run app.py --server.port 8502` |
| Import error | Reinstall in correct Python environment |
| Styling broken | Hard refresh browser (Ctrl+Shift+R) |

---

## System Requirements

### Minimum
- Python 3.8+
- 2 GB RAM
- Internet connection (for map tiles)
- Modern web browser

### Recommended
- Python 3.9+
- 4 GB RAM
- Stable internet
- Chrome or Firefox browser
- 1920x1080 screen resolution

---

## Testing Checklist

Before demo, verify:
- [ ] Application starts without errors
- [ ] All villages load on map
- [ ] Risk scores display correctly
- [ ] Charts render properly
- [ ] Mode switching works
- [ ] Language selection works
- [ ] All sections visible
- [ ] No console errors (F12)

---

## Emergency Demo Backup

If live demo fails:
1. **Screenshots ready**: Take screenshots of all features
2. **Video backup**: Record screen showing features
3. **Explain verbally**: Walk through features without showing
4. **Local backup**: Have app running on another machine

---

## Contact & Support

For technical issues during competition:
- Document all errors with screenshots
- Note exact error messages
- Record browser console output (F12)
- Have system info ready (Python version, OS, etc.)

---

**Remember: Most issues are environment-related. A clean Python virtual environment solves 80% of problems!**

```bash
# Nuclear option - fresh start
python3 -m venv clean_env
source clean_env/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

**Good luck! 🚀**
