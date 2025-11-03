import pandas as pd

df = pd.read_csv("checked5.csv")

if "Missing Link" in df.columns:
    df = df.drop(columns=["Missing Link"])

df.to_csv("checked52.csv", index=False, encoding="utf-8")

print(f"✅ ' checked52.csv")
