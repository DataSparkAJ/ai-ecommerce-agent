import pandas as pd

def analysis_tool(df: pd.DataFrame) -> dict:
    summary = {}

    # Basic KPIs
    summary["total_sales"] = float(df["Sales"].sum())
    summary["total_profit"] = float(df["Profit"].sum())
    summary["avg_order_value"] = float(df["Sales"].mean())

    # Profit Margin %
    df["profit_margin"] = (df["Profit"] / df["Sales"]) * 100
    summary["avg_profit_margin"] = float(df["profit_margin"].mean())

    # Region-wise Sales
    if "Region" in df.columns:
        summary["sales_by_region"] = (
            df.groupby("Region")["Sales"].sum().sort_values(ascending=False).to_dict()
        )

    # Category-wise Profit
    if "Category" in df.columns:
        summary["profit_by_category"] = (
            df.groupby("Category")["Profit"].sum().sort_values(ascending=False).to_dict()
        )

    # Discount Impact
    summary["discount_impact"] = float(
        df.groupby("Discount")["Profit"].mean().corr(df.groupby("Discount")["Sales"].mean())
    ) if "Discount" in df.columns else None

    return summary
