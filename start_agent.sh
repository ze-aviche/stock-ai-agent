#!/bin/bash

# Trading Advisor Agent Startup Script

echo "🤖 Starting Trading Advisor Agent..."
echo "======================================"

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "❌ Virtual environment not found. Please run setup first."
    exit 1
fi

# Activate virtual environment
source venv/bin/activate

# Check for required environment variables
if [ -z "$GOOGLE_API_KEY" ]; then
    echo "❌ GOOGLE_API_KEY environment variable not set"
    echo "Please set it with: export GOOGLE_API_KEY='your-api-key-here'"
    exit 1
fi

# Check for required API keys
if [ -z "$ALPACA_API_KEY" ] || [ -z "$ALPACA_SECRET_KEY" ]; then
    echo "⚠️  Warning: ALPACA_API_KEY or ALPACA_SECRET_KEY not set"
    echo "Trading functionality may be limited"
fi

if [ -z "$POLYGON_API_KEY" ]; then
    echo "⚠️  Warning: POLYGON_API_KEY not set"
    echo "Market data functionality may be limited"
fi

# Initialize database if needed
echo "📊 Checking database..."
python db/init_trades_db.py

# Start the agent
echo "🚀 Starting agent..."
python run_agent.py 