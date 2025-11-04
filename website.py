import streamlit as st
import pandas as pd

# ======================
# 🚀 高速加载 + 缓存数据
# ======================
@st.cache_data
def load_data():
    df = pd.read_csv("checked52.csv")
    df.columns = [c.strip() for c in df.columns]
    for col in ["job_title", "company", "location", "job_link"]:
        if col in df.columns:
            df[col] = df[col].fillna("N/A")
    # 提前创建 lower 列方便搜索
    df["job_title_lower"] = df["job_title"].str.lower()
    df["company_lower"] = df["company"].str.lower()

    # 转换标签列
    df["Work Type Label"] = df["Remote or Not"].map({"yes": "Remote", "no": "On-site"})
    df["Employer Type Label"] = df["Non-profit or Not"].map({"yes": "Non-profit", "no": "Private"})

    return df

df = load_data()

# ======================
# 🌍 页面设置
# ======================
st.set_page_config(page_title="PIT-NE", page_icon="🌍", layout="wide")
st.title("🌍 PIT-NE — Public Interest Technology Job Explorer")

st.sidebar.header("🔎 Filter Jobs")

# ======================
# 🎛️ 筛选器
# ======================
search_text = st.sidebar.text_input("Search jobs by keyword:")

work_options = ["Remote", "On-site"]
selected_work = st.sidebar.multiselect("Work Type", work_options)

employer_options = ["Non-profit", "Private"]
selected_employer = st.sidebar.multiselect("Employer Type", employer_options)

domain_cols = [
    "Policy & Governance", "Ethics & Responsible Tech", "Cybersecurity & Privacy",
    "Civic Tech & Social Impact", "Nonprofit & Philanthropy",
    "STEM", "Arts", "Humanities", "Other"
]
selected_domains = st.sidebar.multiselect("Job Domain", domain_cols)

# ======================
# 🧮 过滤逻辑
# ======================
filtered_df = df.copy()

# 搜索关键词
if search_text:
    s = search_text.lower()
    filtered_df = filtered_df[
        filtered_df["job_title_lower"].str.contains(s, na=False)
        | filtered_df["company_lower"].str.contains(s, na=False)
    ]

# 工作类型过滤
if selected_work:
    filtered_df = filtered_df[filtered_df["Work Type Label"].isin(selected_work)]

# 雇主类型过滤
if selected_employer:
    filtered_df = filtered_df[filtered_df["Employer Type Label"].isin(selected_employer)]

# 领域过滤
if selected_domains:
    mask = (filtered_df[selected_domains] == "yes").any(axis=1)
    filtered_df = filtered_df[mask]

# ======================
# 📄 分页显示结果
# ======================
results_per_page = 20
total_results = len(filtered_df)
total_pages = max((total_results - 1) // results_per_page + 1, 1)
page = st.sidebar.number_input("Page", 1, total_pages, 1)

start = (page - 1) * results_per_page
end = start + results_per_page
page_df = filtered_df.iloc[start:end]

st.markdown(f"### Showing {len(page_df)} of {total_results} job results")

# ======================
# 💼 展示结果卡片
# ======================
for _, row in page_df.iterrows():
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
