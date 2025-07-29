# Trading Advisor Agent - Usage Guide

## 🚀 Quick Start

### 1. Set Environment Variables
```bash
export GOOGLE_API_KEY="your-google-api-key"
export ALPACA_API_KEY="your-alpaca-api-key"
export ALPACA_SECRET_KEY="your-alpaca-secret-key"
export POLYGON_API_KEY="your-polygon-api-key"
```

### 2. Start the Agent
```bash
./start_agent.sh
```

Or manually:
```bash
source venv/bin/activate
python run_agent.py
```

## 🤖 Agent Capabilities

The Trading Advisor Agent is a comprehensive AI-powered trading system that can:

### **1. Gap-Up Stock Identification**
- Identify stocks that have gapped up significantly
- Filter by price, volume, and other criteria
- Provide real-time gap-up analysis

### **2. Historical Pattern Analysis**
- Analyze historical gap-up days for specific stocks
- Provide detailed tabular data for each gap-up day
- Calculate success rates and pattern tendencies

### **3. Trade Planning**
- Generate comprehensive trade plans based on analysis
- Include entry/exit criteria, risk management
- Provide confidence levels and strategy rationale

### **4. Trade Execution**
- Execute trades on Alpaca paper trading platform
- Support market, limit, and stop orders
- Continuous monitoring for entry/exit conditions
- Comprehensive trade logging

## 📊 Example Interactions

### **Identify Gap-Up Stocks**
```
You: Find today's gap-up stocks
Agent: [Lists stocks with gap-up percentages and analysis]
```

### **Analyze Historical Data**
```
You: Analyze historical gap-up data for AAPL
Agent: [Provides detailed tabular data and summary analysis]
```

### **Plan a Trade**
```
You: Plan a trade for LIDR based on today's gap-up
Agent: [Provides comprehensive trade plan with entry/exit criteria]
```

### **Execute a Trade**
```
You: Execute the trade plan for LIDR
Agent: [Executes trade and provides confirmation]
```

## 🔧 System Components

### **Agents**
- **Gap-Up Identification Agent**: Identifies potential gap-up stocks
- **Data Analysis Agent**: Analyzes historical patterns and data
- **Trade Planning Agent**: Creates comprehensive trade plans
- **Execution Agent**: Executes trades on Alpaca

### **Databases**
- **trades.db**: Comprehensive trade logging and tracking
- **ticker_details.db**: Stock information and details

### **APIs**
- **Polygon.io**: Real-time and historical market data
- **Alpaca**: Paper trading execution
- **Google AI**: LLM capabilities for analysis and planning

## 🛠️ Troubleshooting

### **Common Issues**

1. **API Key Errors**
   - Ensure all environment variables are set
   - Check API key validity and permissions

2. **Database Errors**
   - Run `python db/init_trades_db.py` to initialize databases
   - Check file permissions for database files

3. **Import Errors**
   - Ensure virtual environment is activated
   - Install missing dependencies: `pip install -r requirements.txt`

4. **ADK Configuration Errors**
   - Use `run_agent.py` instead of `adk run` (ADK YAML config not ready)
   - The direct Python script bypasses ADK configuration issues

## 📈 Continuous Monitoring

The system supports continuous monitoring for trade execution:

- **Automatic Entry**: Monitors prices and executes when entry criteria are met
- **Risk Management**: Automatically places stop-loss and take-profit orders
- **Trade Logging**: Comprehensive logging of all trade activities
- **Status Tracking**: Real-time status updates for all active trades

## 🔒 Safety Features

- **Paper Trading Only**: All trades are executed on Alpaca paper trading
- **Risk Management**: Built-in stop-loss and take-profit mechanisms
- **Trade Validation**: Multiple validation checks before execution
- **Comprehensive Logging**: Full audit trail of all trading activities

## 📝 Notes

- The system uses Alpaca paper trading for safety
- All trades are logged to the local SQLite database
- Historical analysis is based on Polygon.io data
- The agent uses Google's Gemini models for analysis and planning

For more information, see the main README.md file. 