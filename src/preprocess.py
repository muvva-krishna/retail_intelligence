# ==========================================
# Data Preprocessing Module
# ==========================================

import pandas as pd


def load_and_clean_data(path: str) -> pd.DataFrame:
    df = pd.read_excel(path)

    # Remove cancelled invoices
    df = df[~df["InvoiceNo"].astype(str).str.startswith("C")]

    # Remove invalid rows
    df = df[df["Quantity"] > 0]
    df = df.dropna(subset=["CustomerID"])

    # Convert types safely
    df["CustomerID"] = df["CustomerID"].astype(int)
    df["Quantity"] = df["Quantity"].astype(int)
    df["UnitPrice"] = df["UnitPrice"].astype(float)

    # Convert datetime
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

    # Feature engineering
    df["Revenue"] = df["Quantity"] * df["UnitPrice"]
    df["YearMonth"] = df["InvoiceDate"].dt.to_period("M").astype(str)

    return df


def compute_kpis(df: pd.DataFrame) -> dict:
    return {
        "total_revenue": df["Revenue"].sum(),
        "top_country": df.groupby("Country")["Revenue"]
                        .sum()
                        .sort_values(ascending=False)
                        .head(1),
        "monthly_revenue": df.groupby("YearMonth")["Revenue"].sum()
    }
