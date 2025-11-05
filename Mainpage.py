import streamlit as st
import base64

def get_base64_of_bin_file(bin_file):
    with open(bin_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

logo_base64 = get_base64_of_bin_file("PIT-NE logo.png")

st.set_page_config(page_title="PIT-NE Jobs", page_icon="PIT-NE logo.png", layout="wide")

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
    .nav-right a {{
        margin-left: 1.5rem;
        text-decoration: none;
        font-weight: 500;
        color: #1b3b75;
    }}
    .nav-right a:hover {{
        text-decoration: underline;
        color: #004aad;
    }}
    </style>

    <div class="nav-container">
        <div class="nav-left">
            <!--  -->
            <img src="data:image/png;base64,{logo_base64}" alt="PIT-NE Logo">
            <div class="nav-title">PIT-NE Jobs</div>
        </div>
        <div class="nav-right">
            <a href="#home">Home</a>
            <a href="https://your-about-page-link" target="_blank">About Us</a>
            <a href="https://multiverse-w9fva7qcna2joe224ixqbe.streamlit.app/" target="_blank">Explore Jobs</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ======== Hero Section ========
st.markdown("<a name='home'></a>", unsafe_allow_html=True)
col1, col2 = st.columns([2, 1])
with col1:
    st.title("Find Your Path in Public Interest Technology")
    st.write(
        "Discover jobs that combine **technology**, **ethics**, and **social impact**. "
        "Join a growing community shaping a more responsible and equitable tech future."
    )
    st.markdown(
        "[🔎 Explore Jobs](https://multiverse-w9fva7qcna2joe224ixqbe.streamlit.app/)",
        unsafe_allow_html=True,
    )
with col2:
    st.image("PIT-NE logo.png", use_container_width=True)

st.markdown("---")

# ======== Careers & Purpose Section ========
st.markdown("## 🌟 Our Focus Areas")

col1, col2 = st.columns(2)

with col1:
    st.image("career_logo.png", width=120)
    st.subheader("Careers")
    st.write(
        "We connect people with meaningful opportunities to use technology for social good. "
        "Our platform helps individuals discover roles where innovation meets ethics, "
        "building a future that prioritizes equity, inclusion, and the public interest."
    )

with col2:
    st.image("Purpose_logo.png", width=120)
    st.subheader("Purpose")
    st.write(
        "PIT-NE was founded with a simple mission: to inspire and empower people to design, "
        "develop, and apply technology that serves humanity — ensuring progress aligns with values."
    )

st.markdown("---")
st.caption("© 2025 PIT-NE — Public Interest Technology Network Explorer")
