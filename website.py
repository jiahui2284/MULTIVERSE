import streamlit as st
import pandas as pd
import base64
import os

# ======================
# ===== Helper =====
def image_to_base64(path):
    if not os.path.exists(path):
        return ""
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# ====== Load Logo ======
logo_base64 = image_to_base64("PIT-NE logo.png")

# ======================
# ===== Data Load =====
@st.cache_data
def load_data():
    df = pd.read_csv("checked52.csv")
    df.columns = [c.strip() for c in df.columns]

    for col in ["job_title", "company", "location", "job_link"]:
        if col in df.columns:
            df[col] = df[col].fillna("N/A")

    df["job_title_lower"] = df["job_title"].str.lower()
    df["company_lower"] = df["company"].str.lower()

    df["Work Type Label"] = df["Work Type"]
    df["Employer Type Label"] = df["Employer Type"]

    return df

df = load_data()

# ======================
# ===== Page Config =====
st.set_page_config(
    page_title="PIT-NE Job Explorer",
    page_icon="PIT-NE logo.png", 
    layout="wide"
)

# ======================
# ===== Navigation Bar =====
st.markdown(
    f"""
    <style>
    .nav-container {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        background-color: #f5f8fc;
        padding: 1rem 2rem;
        border-bottom: 1px solid #e1e4e8;
        position: sticky;
        top: 0;
        z-index: 100;
    }}
    .nav-left {{
        display: flex;
        align-items: center;
        gap: 0.75rem;
    }}
    .nav-left img {{
        height: 50px;
    }}
    .nav-title {{
        font-weight: 700;
        font-size: 1.4rem;
        color: #1b3b75;
    }}
    .nav-right {{
        display: flex;
        align-items: center;
    }}
    .nav-right a {{
        margin-left: 1.5rem;
        text-decoration: none;
        font-weight: 500;
        color: #1b3b75;
        padding: 0.4rem 0.8rem;
        border-radius: 8px;
        transition: all 0.2s ease-in-out;
    }}
    .nav-right a:hover {{
        background-color: #004aad;
        color: white;
        text-decoration: none;
    }}
    .nav-right a.active {{
        background-color: #004aad;
        color: white;
        font-weight: 600;
    }}
    </style>

    <div class="nav-container">
        <div class="nav-left">
            <img src="data:image/png;base64,{logo_base64}" alt="PIT-NE Logo">
            <div class="nav-title">PIT-NE Job Explorer</div>
        </div>
        <div class="nav-right">
            <a href="https://multiverse-fsbeuhmjvnyfbdzyhbaemt.streamlit.app/" target="_blank">🏠 Home</a>
            <a href="https://multiverse-fnzxuryfjyfezrv523ypq5.streamlit.app/" target="_blank">About Us</a>
            <a class="active" href="#" target="_self">Explore Jobs</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ======================
# ===== Sidebar Filters =====
st.sidebar.header("🔎 Filter Jobs")

search_text = st.sidebar.text_input("Search jobs by keyword:")

work_options = sorted(df["Work Type Label"].dropna().unique().tolist())
selected_work = st.sidebar.multiselect("Work Type", work_options)

employer_options = sorted(df["Employer Type Label"].dropna().unique().tolist())
selected_employer = st.sidebar.multiselect("Employer Type", employer_options)

# ===== Seniority Filter =====
if "Seniority" in df.columns:
    seniority_options = [
        "Entry",
        "Mid",
        "Senior IC",
        "Senior Manager",
        "Director",
        "Executive",
        "Unknown"
    ]
    selected_seniority = st.sidebar.multiselect("Seniority Level", seniority_options)
else:
    selected_seniority = []
# Domain columns
base_cols = [
    "job_title", "company", "location", "job_link",
    "has_keyword", "Work Type", "Employer Type",
    "job_title_lower", "company_lower",
    "Work Type Label", "Employer Type Label", "Seniority"
]
domain_cols = [c for c in df.columns if c not in base_cols]

selected_domains = st.sidebar.multiselect("Job Domain", domain_cols)

# ======================
# ===== Data Filter =====
filtered_df = df.copy()

if search_text:
    s = search_text.lower()
    filtered_df = filtered_df[
        filtered_df["job_title_lower"].str.contains(s, na=False)
        | filtered_df["company_lower"].str.contains(s, na=False)
    ]

if selected_work:
    filtered_df = filtered_df[filtered_df["Work Type Label"].isin(selected_work)]

if selected_employer:
    filtered_df = filtered_df[filtered_df["Employer Type Label"].isin(selected_employer)]

if selected_domains:
    mask = (filtered_df[selected_domains] == "yes").any(axis=1)
    filtered_df = filtered_df[mask]

if selected_seniority:
    filtered_df = filtered_df[filtered_df["Seniority"].isin(selected_seniority)]

# ======================
# ===== Pagination =====
results_per_page = 10
total_results = len(filtered_df)
total_pages = max((total_results - 1) // results_per_page + 1, 1)
page = st.sidebar.number_input("Page", 1, total_pages, 1)

start = (page - 1) * results_per_page
end = start + results_per_page
page_df = filtered_df.iloc[start:end]

st.markdown(f"### Showing {len(page_df)} of {total_results} job results")

# ======================
# ===== Job Cards =====
for _, row in page_df.iterrows():
    st.markdown("---")
    st.subheader(row["job_title"])

    col1, col2, col3, col4, col5 = st.columns([2, 2, 2, 2, 2])

    with col1:
        st.write(f"🏢 **Employer:** {row['company']}")
    with col2:
        st.write(f"📍 **Location:** {row.get('location', 'N/A')}")
    with col3:
        st.write(f"💼 **Work Type:** {row['Work Type Label']}")
    with col4:
        st.write(f"🏢 **Employer Type:** {row['Employer Type Label']}")
    with col5:
        st.write(f"📊 **Seniority:** {row.get('Seniority', 'Unknown')}")

    st.markdown(f"[🟢 Apply Here]({row['job_link']})", unsafe_allow_html=True)

st.markdown("---")
st.caption("© 2025 PIT-NE — Public Interest Technology Network Explorer")