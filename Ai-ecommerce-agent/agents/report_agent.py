from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image,
    PageBreak,
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors


def _footer(canvas, doc):
    """Footer on every page."""
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.HexColor("#5A189A"))  # midnight purple
    footer_text = "✦ Powered by Gemini | Author: Ajay Singh ✦"
    canvas.drawCentredString(A4[0] / 2.0, 15, footer_text)
    canvas.restoreState()


def _clean_insights_text(text: str) -> str:
    """
    Gemini jo markdown deta hai (###, **, * etc),
    usko clean karke PDF ke Paragraph ke liye simple HTML jaisa banate hain.
    """
    if not text:
        return ""

    t = text

    # Remove markdown headings symbols
    t = t.replace("#####", "")
    t = t.replace("####", "")
    t = t.replace("###", "")
    t = t.replace("##", "")
    t = t.replace("#", "")

    # Bold markers remove (simple way)
    t = t.replace("**", "")

    # Bullet points: "* " -> "• "
    t = t.replace("\n* ", "\n• ")
    if t.startswith("* "):
        t = "• " + t[2:]

    # Convert line breaks to <br/> so ReportLab Paragraph can handle
    t = t.replace("\r\n", "\n")
    t = t.replace("\r", "\n")
    t = t.replace("\n\n", "<br/><br/>")
    t = t.replace("\n", "<br/>")

    return t


def report_agent(summary: dict, insights: str, chart_paths):
    """
    Final styled PDF generate karega.
    A4 portrait layout, clean sections, footer, aur basic icons.
    """
    file_name = "AI_Ecommerce_Insight_Agent_Report.pdf"

    doc = SimpleDocTemplate(
        file_name,
        pagesize=A4,
        leftMargin=40,
        rightMargin=40,
        topMargin=60,
        bottomMargin=40,
    )

    styles = getSampleStyleSheet()
    # Title style
    styles.add(
        ParagraphStyle(
            name="ReportTitle",
            parent=styles["Title"],
            fontName="Helvetica-Bold",
            fontSize=22,
            textColor=colors.HexColor("#5A189A"),  # midnight purple
            alignment=1,  # center
            spaceAfter=20,
        )
    )
    # Section heading style
    styles.add(
        ParagraphStyle(
            name="SectionHeading",
            parent=styles["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=14,
            textColor=colors.HexColor("#5A189A"),
            spaceBefore=12,
            spaceAfter=6,
        )
    )
    # Normal body text
    styles.add(
        ParagraphStyle(
            name="BodyTextCustom",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=11,
            leading=16,
        )
    )
    # KPI text
    styles.add(
        ParagraphStyle(
            name="KPIText",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=11,
            leading=15,
            leftIndent=10,
        )
    )

    elements = []

    # ------------- COVER PAGE -------------
    elements.append(Spacer(1, 2 * inch))
    elements.append(Paragraph("AI Ecommerce Insight Agent Report", styles["ReportTitle"]))
    elements.append(Spacer(1, 0.3 * inch))
    subtitle = "Data-driven sales & profit insights generated using AI agents."
    elements.append(Paragraph(subtitle, styles["BodyTextCustom"]))
    elements.append(PageBreak())

    # ------------- KEY BUSINESS KPIs -------------
    elements.append(
        Paragraph("📊 Key Business KPIs", styles["SectionHeading"])
    )

    # Separate scalar KPIs and dict-based
    scalar_items = {}
    dict_items = {}
    for k, v in summary.items():
        if isinstance(v, dict):
            dict_items[k] = v
        else:
            scalar_items[k] = v

    # Scalar KPIs as simple list
    for k, v in scalar_items.items():
        elements.append(
            Paragraph(f"<b>{k.replace('_', ' ').title()}:</b> {v}", styles["KPIText"])
        )

    elements.append(Spacer(1, 0.2 * inch))

    # Dict KPIs (like sales_by_region, profit_by_category)
    for k, d in dict_items.items():
        elements.append(
            Paragraph(
                f"• <b>{k.replace('_', ' ').title()}:</b>",
                styles["BodyTextCustom"],
            )
        )
        if isinstance(d, dict):
            for key2, val2 in d.items():
                elements.append(
                    Paragraph(
                        f"&nbsp;&nbsp;&nbsp;– {key2}: {val2}",
                        styles["BodyTextCustom"],
                    )
                )
        elements.append(Spacer(1, 0.1 * inch))

    elements.append(Spacer(1, 0.3 * inch))

    # ------------- AI GENERATED INSIGHTS -------------
    elements.append(
        Paragraph("🧠 AI-Generated Business Insights", styles["SectionHeading"])
    )

    cleaned_insights = _clean_insights_text(insights)
    elements.append(Paragraph(cleaned_insights, styles["BodyTextCustom"]))

    elements.append(PageBreak())

    # ------------- VISUAL ANALYSIS (CHARTS) -------------
    elements.append(
        Paragraph("📈 Visual Analysis", styles["SectionHeading"])
    )

    if chart_paths:
        for path in chart_paths:
            try:
                elements.append(Image(path, width=5.5 * inch, height=3.2 * inch))
                elements.append(Spacer(1, 0.2 * inch))
            except Exception as e:
                # Agar koi chart load nahi hota, just skip
                elements.append(
                    Paragraph(
                        f"(Could not load chart: {path})",
                        styles["BodyTextCustom"],
                    )
                )
                elements.append(Spacer(1, 0.1 * inch))
    else:
        elements.append(
            Paragraph("No charts generated by VizAgent.", styles["BodyTextCustom"])
        )

    # ------------- BUILD PDF -------------
    doc.build(elements, onFirstPage=_footer, onLaterPages=_footer)

    print(f"[LOG] PDF created successfully: {file_name}")
    return file_name
