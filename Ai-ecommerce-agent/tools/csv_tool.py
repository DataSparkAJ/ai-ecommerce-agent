import pandas as pd

def load_csv_tool(path: str) -> pd.DataFrame:
    print(f"[LOG] Loading dataset from: {path}")
    df = pd.read_csv(path)
    print(f"[LOG] Dataset rows: {df.shape[0]}, columns: {df.shape[1]}")
    return df
