from tools.csv_tool import load_csv_tool
import pandas as pd

def data_agent(path: str) -> pd.DataFrame:
    df = load_csv_tool(path)

    df.drop_duplicates(inplace=True)

    # Convert dates (day first = True to remove warning)
    for col in ["Order Date", "Ship Date"]:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors="coerce", dayfirst=True)

    # Numeric columns
    num_cols = ["Sales", "Quantity", "Discount", "Shipping Cost", "Profit"]
    for col in num_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    print("[LOG] DataAgent finished cleaning.")
    return df
