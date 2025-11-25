from tools.viz_tool import viz_tool
import pandas as pd

def viz_agent(df: pd.DataFrame):
    print("[LOG] Running VizAgent...")
    chart_paths = viz_tool(df)
    print("[LOG] VizAgent finished.")
    return chart_paths
