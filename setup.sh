#!/bin/bash

# NER-Aegis AI - Setup Script
# This script automates the installation and launch of NER-Aegis AI

echo "╔══════════════════════════════════════════════════════════╗"
echo "║                                                          ║"
echo "║         🏔️  NER-Aegis AI Setup Script                   ║"
echo "║     Autonomous Landslide Risk Intelligence System        ║"
echo "║                                                          ║"
echo "╚══════════════════════════════════════════════════════════╝"
echo ""

# Check if Python is installed
echo "🔍 Checking Python installation..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d" " -f2 | cut -d"." -f1,2)
echo "✅ Found Python $PYTHON_VERSION"
echo ""

# Check if pip is installed
echo "🔍 Checking pip installation..."
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 is not installed. Please install pip."
    exit 1
fi
echo "✅ pip3 is installed"
echo ""

# Install dependencies
echo "📦 Installing dependencies..."
echo "   This may take a minute..."
pip3 install -r requirements.txt --quiet

if [ $? -eq 0 ]; then
    echo "✅ All dependencies installed successfully!"
else
    echo "❌ Error installing dependencies. Please check your internet connection."
    exit 1
fi
echo ""

# Success message
echo "╔══════════════════════════════════════════════════════════╗"
echo "║                                                          ║"
echo "║              ✅ Setup Complete! ✅                        ║"
echo "║                                                          ║"
echo "╚══════════════════════════════════════════════════════════╝"
echo ""
echo "🚀 Starting NER-Aegis AI..."
echo ""
echo "📱 The application will open in your default browser."
echo "   If it doesn't, navigate to: http://localhost:8501"
echo ""
echo "💡 Demo Tips:"
echo "   1. Start with 'Disaster Officer' mode"
echo "   2. Explore the overview dashboard"
echo "   3. Select 'Cherrapunji' for high-risk scenario"
echo "   4. Check out the micro-evacuation planning"
echo "   5. Switch to 'Citizen View' to see simplified interface"
echo ""
echo "⚠️  Remember: This provides risk intelligence, NOT prediction"
echo ""
echo "Press Ctrl+C to stop the application"
echo "─────────────────────────────────────────────────────────"
echo ""

# Launch the application
streamlit run app.py
