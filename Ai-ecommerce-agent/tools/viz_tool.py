import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import plotly.express as px

def plot_static_charts(df: pd.DataFrame):
    chart_paths = []

    # ---- Profit by Category ---- #
    if "Category" in df.columns:
        plt.figure(figsize=(6, 4))
        df.groupby("Category")["Profit"].sum().plot(kind="bar")
        plt.title("Profit by Category")
        plt.ylabel("Total Profit")
        plt.tight_layout()
        path = "profit_by_category.png"
        plt.savefig(path, dpi=120, bbox_inches="tight")
        chart_paths.append(path)
        plt.show()
        plt.close()

    # ---- Discount vs Profit Margin ---- #
    if "Discount" in df.columns:
        temp = df.copy()
        temp["profit_margin"] = (temp["Profit"] / temp["Sales"]) * 100
        plt.figure(figsize=(6, 4))
        sns.scatterplot(data=temp, x="Discount", y="profit_margin")
        plt.title("Discount Impact on Profit Margin")
        plt.tight_layout()
        path = "discount_vs_margin.png"
        plt.savefig(path, dpi=120, bbox_inches="tight")
        chart_paths.append(path)
        plt.show()

    return chart_paths


def plot_interactive_charts(df: pd.DataFrame):
    return
    # ---- Sales by Region ---- #
    if "Region" in df.columns:
        region = df.groupby("Region")["Sales"].sum().reset_index()
        fig1 = px.bar(region, x="Region", y="Sales", title="Sales by Region")
        fig1.show()

    # ---- Sales by Category ---- #
    if "Category" in df.columns:
        cat = df.groupby("Category")["Sales"].sum().reset_index()
        fig2 = px.pie(cat, names="Category", values="Sales",
                      title="Sales Distribution by Category")
        fig2.show()


def viz_tool(df: pd.DataFrame):
    print("[LOG] Creating static charts...")
    chart_paths = plot_static_charts(df)
    print("[LOG] Static charts created and saved:", chart_paths)

    print("[LOG] Skipping interactive charts temporarily...")
    # plot_interactive_charts(df)
    print("[LOG] Interactive charts skipped.")

    return chart_paths
