#!/bin/bash

# LegalAI Simplifier Deployment Script
# For Google Gen AI Exchange Hackathon

echo "🚀 Deploying LegalAI Simplifier..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed."
    exit 1
fi

# Check if pip is installed
if ! command -v pip &> /dev/null; then
    echo "❌ pip is required but not installed."
    exit 1
fi

# Install requirements
echo "📦 Installing dependencies..."
pip install -r requirements.txt

# Check if Streamlit is installed
if ! command -v streamlit &> /dev/null; then
    echo "❌ Streamlit installation failed."
    exit 1
fi

echo "✅ Dependencies installed successfully!"

# Run the application
echo "🎯 Starting LegalAI Simplifier..."
echo "🌐 Access the app at: http://localhost:8501"
echo "⚖️ Making legal documents accessible to everyone!"
echo ""

streamlit run app.py
