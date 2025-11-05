import streamlit as st

st.set_page_config(page_title="PIT-NE Jobs", page_icon="PIT-NE logo.png", layout="wide")

st.markdown(
    """
    <style>
    .nav-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background-color: #f5f8fc;
        padding: 1rem 2rem;
        border-bottom: 1px solid #e1e4e8;
        position: sticky;
        top: 0;
        z-index: 100;
    }
    .nav-left {
        display: flex;
        align-items: center;
        gap: 0.75rem;
    }
    .nav-left img {
        height: 50px;
    }
    .nav-title {
        font-weight: 700;
        font-size: 1.4rem;
        color: #1b3b75;
    }
    .nav-right a {
        margin-left: 1.5rem;
        text-decoration: none;
        font-weight: 500;
        color: #1b3b75;
    }
    .nav-right a:hover {
        text-decoration: underline;
        color: #004aad;
    }
    </style>

    <div class="nav-container">
        <div class="nav-left">
            <img src="PIT-NE logo.png" alt="PIT-NE Logo">
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

# ========== Hero Section（主标题部分） ==========
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

st.markdown(
    """
    <style>
    .section-container {
        display: flex;
        justify-content: center;
        align-items: flex-start;
        gap: 5rem;
        margin-top: 2rem;
        flex-wrap: wrap;
    }
    .card {
        text-align: center;
        width: 260px;
    }
    .card img {
        height: 90px;
        margin-bottom: 1rem;
    }
    .card h3 {
        color: #1b3b75;
        margin-bottom: 0.5rem;
    }
    .card p {
        color: #333333;
        font-size: 0.95rem;
    }
    </style>

    <div class="section-container">
        <div class="card">
            <img src="career_logo.png" alt="Careers">
            <h3>Careers</h3>
            <p>We connect people with opportunities to build technology for public good.</p>
        </div>
        <div class="card">
            <img src="Purpose_logo.png" alt="Purpose">
            <h3>Purpose</h3>
            <p>Our mission is to inspire and empower ethical technology for everyone.</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("---")
st.caption("© 2025 PIT-NE — Public Interest Technology Network Explorer")
