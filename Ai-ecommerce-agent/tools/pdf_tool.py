from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4

def pdf_tool(filename: str,
             summary: dict,
             insight_text: str,
             chart_paths: list | None = None):
    print("[LOG] Generating PDF:", filename)

    styles = getSampleStyleSheet()
    story = []

    # Title
    story.append(Paragraph("E-Commerce Sales Insights Report", styles["Title"]))
    story.append(Spacer(1, 16))

    # KPIs section (short, business style)
    story.append(Paragraph("Key Metrics (KPIs)", styles["Heading2"]))
    for key in ["total_sales", "total_profit", "avg_order_value",
                "avg_profit_margin"]:
        if key in summary:
            story.append(Paragraph(f"{key.replace('_', ' ').title()}: "
                                   f"{round(summary[key], 2)}", styles["Normal"]))
    story.append(Spacer(1, 12))

    # Region and Category (if present)
    if "sales_by_region" in summary:
        story.append(Paragraph("Sales by Region (top few)", styles["Heading3"]))
        for region, val in list(summary["sales_by_region"].items())[:6]:
            story.append(Paragraph(f"{region}: {round(val, 2)}", styles["Normal"]))
        story.append(Spacer(1, 8))

    if "profit_by_category" in summary:
        story.append(Paragraph("Profit by Category", styles["Heading3"]))
        for cat, val in summary["profit_by_category"].items():
            story.append(Paragraph(f"{cat}: {round(val, 2)}", styles["Normal"]))
        story.append(Spacer(1, 12))

    # Insights section (hybrid: bullets + explanation)
    story.append(Paragraph("AI-Generated Insights & Recommendations",
                           styles["Heading2"]))
    for line in insight_text.split("\n"):
        if line.strip():
            story.append(Paragraph(line.strip(), styles["Normal"]))
            story.append(Spacer(1, 4))

    # Charts
    if chart_paths:
        story.append(Spacer(1, 16))
        story.append(Paragraph("Visuals", styles["Heading2"]))
        story.append(Spacer(1, 8))
        for path in chart_paths:
            try:
                story.append(Image(path, width=400, height=250))
                story.append(Spacer(1, 12))
            except Exception as e:
                print(f"[WARN] Could not add image {path}: {e}")

    doc = SimpleDocTemplate(filename, pagesize=A4)
    doc.build(story)
    print("[LOG] PDF created successfully.")
