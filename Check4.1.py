import pandas as pd

df = pd.read_csv("checked4.csv")

filtered_df = df[df["Missing Link"] != "missing"]


filtered_df.to_csv("checked41.csv", index=False, encoding="utf-8")

print(f" {len(filtered_df)} ）。")
