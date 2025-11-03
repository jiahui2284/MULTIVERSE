import pandas as pd
import matplotlib.pyplot as plt

# === Load dataset ===
df = pd.read_csv("checked52.csv")

# Clean column names
df.columns = [c.strip() for c in df.columns]

# === Define key domains ===
domain_cols = [
    "Policy & Governance", "Ethics & Responsible Tech", "Cybersecurity & Privacy",
    "Civic Tech & Social Impact", "Nonprofit & Philanthropy",
    "STEM", "Arts", "Humanities", "Other"
]

# === 1️⃣ Basic counts ===
remote_counts = df["Remote or Not"].value_counts()
nonprofit_counts = df["Non-profit or Not"].value_counts()
domain_counts = (df[domain_cols] == "yes").sum().sort_values(ascending=False)

# === 2️⃣ Compute domain percentages ===
total_jobs = len(df)
domain_percent = (domain_counts / total_jobs * 100).round(2)

# Combine into a table
domain_summary = pd.DataFrame({
    "Count": domain_counts,
    "Percentage (%)": domain_percent
}).sort_values(by="Count", ascending=False)

# === 3️⃣ Display summary stats ===
print("🔹 Remote vs On-site:")
print(remote_counts, "\n")

print("🔹 Non-profit vs Private:")
print(nonprofit_counts, "\n")

print("🔹 Job Domain Distribution (Count + Percentage):")
print(domain_summary, "\n")

# === 4️⃣ Visualizations ===
plt.figure(figsize=(14, 5))

# Remote vs On-site
plt.subplot(1, 3, 1)
remote_counts.plot(kind="bar", color=["skyblue", "lightcoral"])
plt.title("Remote vs On-site Jobs")
plt.ylabel("Count")

# Non-profit vs Private
plt.subplot(1, 3, 2)
nonprofit_counts.plot(kind="bar", color=["lightgreen", "orange"])
plt.title("Non-profit vs Private Jobs")
plt.ylabel("Count")

# Domain percentages
plt.subplot(1, 3, 3)
domain_percent.plot(kind="barh", color="steelblue")
plt.title("Job Domain Percentage")
plt.xlabel("% of Total Jobs")

plt.tight_layout()
plt.show()

# === 5️⃣ Cross-analysis ===
remote_domain = df.groupby("Remote or Not")[domain_cols].apply(lambda x: (x == "yes").sum())
remote_domain.T.plot(kind="bar", figsize=(10, 5), title="Remote vs On-site across Domains")
plt.ylabel("Number of Jobs")
plt.tight_layout()
plt.show()

nonprofit_domain = df.groupby("Non-profit or Not")[domain_cols].apply(lambda x: (x == "yes").sum())
nonprofit_domain.T.plot(kind="bar", figsize=(10, 5), title="Non-profit vs Private across Domains")
plt.ylabel("Number of Jobs")
plt.tight_layout()
plt.show()

# === 6️⃣ Summary ===
pct_remote = (remote_counts.get("yes", 0) / total_jobs) * 100
pct_nonprofit = (nonprofit_counts.get("yes", 0) / total_jobs) * 100

print("📊 SUMMARY INSIGHTS")
print(f"• Total Jobs: {total_jobs}")
print(f"• Remote Jobs: {pct_remote:.1f}% ({remote_counts.get('yes', 0)} total)")
print(f"• Non-profit Jobs: {pct_nonprofit:.1f}% ({nonprofit_counts.get('yes', 0)} total)")
print("\nTop Job Domains (by share):")
print(domain_summary.head(5), "\n")

print("🧠 INTERPRETATION")
print("- Public Interest Technology jobs appear across technical and governance-focused areas.")
print("- STEM dominates overall, but Policy & Governance and Cybersecurity are strong secondary clusters.")
print("- Ethics & Responsible Tech remains a small but distinct field.")
print("- Non-profit roles concentrate in Civic Tech & Philanthropy, private ones in STEM & Cybersecurity.")
print("- Remote work aligns with technical roles, while civic/policy jobs remain more location-based.\n")

print("✅ Analysis complete — including domain percentages.")

