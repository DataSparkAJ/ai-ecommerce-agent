import google.generativeai as genai

def insight_agent(summary: dict) -> str:
    prompt = f"""
You are a senior business analyst. Using the KPIs below, write insights that help improve e-commerce performance.

Provide:
1) Key business findings
2) Root causes behind patterns
3) Actionable recommendations (5–7 points)
4) Priority categories/regions
5) Pricing and discount strategy suggestions

Dataset KPIs:
{summary}
"""

    print("[LOG] Calling Gemini 2.x...")
    response = genai.GenerativeModel("gemini-2.5-flash").generate_content(prompt)
    print("[LOG] InsightAgent finished.")
    return response.text
