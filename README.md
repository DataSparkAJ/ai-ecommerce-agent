### 🧠 AI Ecommerce Insight Agent
## Multi-Agent Business Intelligence System Powered by Gemini
## 📌 Overview

The AI Ecommerce Insight Agent is a multi-agent analytics workflow that automates e-commerce performance reporting. It replaces manual Excel/Python work by:

* Loading and cleaning e-commerce datasets

* Calculating key sales & profitability metrics

* Generating visual insights (charts)

* Producing a professional multi-page PDF

* Writing strategic insights using Gemini

* Outcome: Fast, reliable business recommendations for pricing, discounting, product categories, and regional growth — without requiring a full-time data analyst.

## ❓ Problem Statement

E-commerce teams rely on raw sales exports from platforms like Shopify, Amazon, and ERP systems. Manual analysis is:

* Time-consuming and repetitive

* Prone to errors

* Limited to surface-level metrics

* Rarely actionable for strategy

* Teams struggle to answer critical questions:

* Which categories actually drive profit?

* Are discounts boosting sales or destroying margin?

* Which regions deserve expansion vs. withdrawal?

* Where is the business leaking profit?

## 💡 Solution

This system uses a multi-agent pipeline to automate business intelligence.

| **Agent**                 | **Responsibility**                  |
| ------------------------- | ----------------------------------- |
| **DataAgent**             | Loads & preprocesses CSV/Excel data |
| **AnalysisAgent**         | Computes KPIs & business metrics    |
| **VizAgent**              | Generates visual charts (PNG)       |
| **InsightAgent (Gemini)** | Writes analyst-grade insights       |
| **ReportAgent**           | Builds the final PDF report         |

## 📌 Only KPI summaries are sent to Gemini
→ Lower cost, faster inference, and focused analysis (context engineering).

## 🏗 Architecture Flow

main.py
   ↓
DataAgent → Load & clean dataset
   ↓
AnalysisAgent → Compute sales & profit KPIs
   ↓
VizAgent → Generate static charts (PNG)
   ↓
InsightAgent (Gemini) → Business insights & strategy
   ↓
ReportAgent → Export multi-page PDF


## 📊 KPIs Generated

* Total Sales

* Total Profit

* Average Order Value (AOV)

* Average Profit Margin

* Discount Impact on Profit

* Sales by Region

* Profit by Category

## 📄 Report Output (PDF Contents)

* KPI Summary

* Analyst-grade Insights

* Root Cause Analysis

* Profitability Recommendations

* Pricing & Discount Strategy

* Region & Category Prioritization

* Visual Charts (PNG)

## ⚙️ Tech Stack

| Component       | Technology                   |
| --------------- | ---------------------------- |
| Language        | Python                       |
| AI Model        | Gemini (google-generativeai) |
| Data Processing | pandas                       |
| Visualization   | matplotlib                   |
| PDF Generation  | reportlab                    |


## 📂 Project Structure

.

├── main.py

├── config.py

├── requirements.txt

│

├── agents/

│   ├── data_agent.py

│   ├── analysis_agent.py

│   ├── viz_agent.py

│   ├── insight_agent.py

│   └── report_agent.py

│

├── tools/

│   ├── analysis_tool.py

│   └── viz_tool.py

│

├── static/

│   └── fonts/

│       ├── Montserrat-Regular.ttf

│       └── Montserrat-Bold.ttf

│

└── (Dataset kept local for privacy)

## ▶️ How to Run

1. Install Requirements
pip install -r requirements.txt

2. Update Dataset Path (inside main.py)  
path = r"D:/your_dataset.csv"

3. Execute
python main.py

4. Enter Gemini API key (requested at runtime, never saved)
##  📁 Outputs Generated

* PDF Report (*.pdf)

* Visual Charts (*.png)

* Terminal Logs ([LOG] ...)

## 🔐 API Security

* API key is collected only via input()

* Never stored or logged

* If exposed, regenerate via Google AI Studio

## 👨‍🎓 Author

Ajay Singh
Individual Participant — Google AI Agents Intensive (5-Day Capstone)
Student & AI Enthusiast

## 📜 License

This project is intended for educational, research, and non-commercial portfolio use.

## Dataset Source:
E-Commerce Website Sales Data — Kaggle
🔗 https://www.kaggle.com/datasets/sivm205/e-commerce-website-sales-data
   
   
