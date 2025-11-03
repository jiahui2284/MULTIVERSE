import pandas as pd


df = pd.read_csv("checked.csv")

df_filtered = df[df["has_keyword"] == "yes"]

#
df_filtered.to_csv("checked0.csv", index=False, encoding="utf-8")

print(f" save to checked0.csv")
