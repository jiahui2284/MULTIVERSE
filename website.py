import streamlit as st
import pandas as pd

# === Load dataset ===
df = pd.read_csv("checked52.csv")

# Clean up column names
df.columns = [c.strip() for c in df.columns]

# Fill missing values
for col in ["job_title", "company", "location", "job_link"]:
    if col in df.columns:
        df[col] = df[col].fillna("N/A")

# === Page setup ===
st.set_page_config(page_title="PIT-NE", page_icon="🌍", layout="wide")
st.title("🌍 PIT-NE — Public Interest Technology Job Explorer")

st.sidebar.header("🔎 Filter Jobs")

# === Sidebar filters ===
# Search bar
search_text = st.sidebar.text_input("Search jobs by keyword:")

# Work Type (map yes/no → Remote / On-site)
df["Work Type Label"] = df["Remote or Not"].map({"yes": "Remote", "no": "On-site"})
work_options = ["Remote", "On-site"]
selected_work = st.sidebar.multiselect("Work Type", work_options)

# Employer Type (map yes/no → Non-profit / Private)
df["Employer Type Label"] = df["Non-profit or Not"].map({"yes": "Non-profit", "no": "Private"})
employer_options = ["Non-profit", "Private"]
selected_employer = st.sidebar.multiselect("Employer Type", employer_options)

# Job Domain options
domain_cols = [
    "Policy & Governance", "Ethics & Responsible Tech", "Cybersecurity & Privacy",
    "Civic Tech & Social Impact", "Nonprofit & Philanthropy",
    "STEM", "Arts", "Humanities", "Other"
]
selected_domains = st.sidebar.multiselect("Job Domain", domain_cols)

# === Filtering logic ===
filtered_df = df.copy()

# Keyword search
if search_text:
    filtered_df = filtered_df[
        filtered_df["job_title"].str.contains(search_text, case=False, na=False)
        | filtered_df["company"].str.contains(search_text, case=False, na=False)
    ]

# Apply Work Type filter
if selected_work:
    filtered_df = filtered_df[filtered_df["Work Type Label"].isin(selected_work)]

# Apply Employer Type filter
if selected_employer:
    filtered_df = filtered_df[filtered_df["Employer Type Label"].isin(selected_employer)]

# Apply Job Domain filter
if selected_domains:
    mask = (filtered_df[selected_domains] == "yes").any(axis=1)
    filtered_df = filtered_df[mask]

# === Display results ===
st.markdown(f"### Showing {len(filtered_df)} job results")

# Job Cards
for _, row in filtered_df.iterrows():
    with st.container():
        st.markdown("---")
        st.subheader(row["job_title"])
        col1, col2, col3, col4 = st.columns([2, 2, 2, 1])
        with col1:
            st.write(f"🏢 **Employer:** {row['company']}")
        with col2:
            st.write(f"📍 **Location:** {row.get('location', 'N/A')}")
        with col3:
            st.write(f"💼 **Work Type:** {row['Work Type Label']}")
        with col4:
            st.write(f"🏢 **Employer Type:** {row['Employer Type Label']}")
        st.markdown(f"[🟢 Apply Here]({row['job_link']})", unsafe_allow_html=True)

st.markdown("---")
st.caption("© 2025 PIT-NE — Public Interest Technology Network Explorer")
