import streamlit as st


st.set_page_config(
    page_title="PIT-NE Jobs",
    page_icon="PIT-NE logo.png",   
    layout="wide"
)


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

    <!-- Top structure-->
    <div class="nav-container">
        <div class="nav-left">
            <!-- ✅ Use logo  -->
            <img src="PIT-NE logo.png" alt="PIT-NE Logo">
            <div class="nav-title">PIT-NE Jobs</div>
        </div>
        <div class="nav-right">
            <a href="#home">Home</a>
            <a href="#about">About Us</a>
            <a href="https://multiverse-w9fva7qcna2joe224ixqbe.streamlit.app/" target="_blank">Explore Jobs</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)


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

    st.markdown("### Explore by Field")
    st.markdown(
        """
        <div style="display:flex;gap:0.5rem;flex-wrap:wrap;">
            <a href="#" style="background:#dce6f7;padding:0.5rem 1rem;border-radius:8px;">STEM</a>
            <a href="#" style="background:#dce6f7;padding:0.5rem 1rem;border-radius:8px;">Humanities</a>
            <a href="#" style="background:#dce6f7;padding:0.5rem 1rem;border-radius:8px;">Policy</a>
            <a href="#" style="background:#dce6f7;padding:0.5rem 1rem;border-radius:8px;">Design</a>
        </div>
        """,
        unsafe_allow_html=True,
    )
with col2:
    st.image("PIT-NE logo.png", use_container_width=True)

st.markdown("---")


st.markdown("<a name='about'></a>", unsafe_allow_html=True)
st.header("About Us")
st.write(
    """
    **PIT-NE (Public Interest Technology – New England)** is a regional network connecting
    people and organizations using technology to serve the public good.

    We believe technology should **advance equity, justice, and inclusion** —
    not just efficiency. Our mission is to help students, educators, and
    professionals find meaningful paths in public-interest-oriented tech careers.
    """
)

st.subheader("Our Vision")
st.write(
    """
    - Empower individuals to use technology for social good  
    - Build partnerships between academia, government, and nonprofits  
    - Create resources that make public-interest tech accessible to all  
    """
)

st.markdown("---")


st.caption("© 2025 PIT-NE — Public Interest Technology Network Explorer")
