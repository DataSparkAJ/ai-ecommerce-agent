from agents.data_agent import data_agent
from agents.analysis_agent import analysis_agent
from agents.viz_agent import viz_agent
from agents.insight_agent import insight_agent
from agents.report_agent import report_agent
from config import configure_gemini

# 1) File path
path = r"D:/PythonJourney/Ai-ecommerce-agent/Dataset/ECOMM DATA.xlsx - Orders.csv"

# 2) Configure Gemini (you will paste key when running)
api_key = input("Enter your Gemini API key (will not be saved): ")
configure_gemini(api_key)

# 3) Run pipeline
df = data_agent(path)
summary = analysis_agent(df)

print("\n===== SUMMARY KPIs =====")
for k, v in summary.items():
    print(k, ":", v)

chart_paths = viz_agent(df)

insights = insight_agent(summary)
print("\n===== AI BUSINESS INSIGHTS (preview) =====")
print(insights[:700], "...\n")  # first part only

pdf_file = report_agent(summary, insights, chart_paths)

print(f"\n[LOG] FULL REPORT SAVED AS: {pdf_file}")
