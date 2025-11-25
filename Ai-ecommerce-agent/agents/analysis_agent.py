from tools.analysis_tool import analysis_tool
import pandas as pd

def analysis_agent(df: pd.DataFrame) -> dict:
    print("[LOG] Running AnalysisAgent...")
    summary = analysis_tool(df)
    print("[LOG] Analysis complete.")
    return summary
