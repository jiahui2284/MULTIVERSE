import streamlit as st
import base64

# =========  =========
def img_to_base64(img_path):
    with open(img_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# =========  =========
logo_b64 = img_to_base64("PIT-NE logo.png")
career_b64 = img_to_base64("career_logo.png")
purpose_b64 = img_to_base64("Purpose_logo.png")
macfound_b64 = img_to_base64("macfound.png")
techcornell_b64 = img_to_base64("techcornell.png")
cdt_b64 = img_to_base64("cdt.png")
napit_b64 = img_to_base64("napit.png")

# =========  =========
st.set_page_config(page_title="PIT-NE Jobs", page_icon="PIT-NE logo.png", layout="wide")

# =========  =========
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
            <img src="data:image/png;base64,{logo_b64}" alt="PIT-NE Logo">
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

# ========= Hero Section =========
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
    st.markdown(f'<img src="data:image/png;base64,{logo_b64}" style="width:100%;">', unsafe_allow_html=True)

st.markdown("---")

# ========= Careers & Purpose Section =========
st.markdown("## 🌟 Our Focus Areas")

col1, col2 = st.columns(2)

with col1:
    st.markdown(f'<img src="data:image/png;base64,{career_b64}" width="120">', unsafe_allow_html=True)
    st.subheader("Careers")
    st.write(
        "We connect people with meaningful opportunities to use technology for social good. "
        "Our platform helps individuals discover roles where innovation meets ethics, "
        "building a future that prioritizes equity, inclusion, and the public interest."
    )

with col2:
    st.markdown(f'<img src="data:image/png;base64,{purpose_b64}" width="120">', unsafe_allow_html=True)
    st.subheader("Purpose")
    st.write(
        "PIT-NE was founded with a simple mission: to inspire and empower people to design, "
        "develop, and apply technology that serves humanity — ensuring progress aligns with values."
    )

# ========= The Latest Section =========
st.markdown(
    """
    <hr style="border: 5px solid #0078d7; margin-top: 3rem; margin-bottom: 1rem;">
    <h2 style="font-size: 2.2rem; font-weight: 700;">The Latest</h2>
    """,
    unsafe_allow_html=True,
)

# ---  ---
col1, col2 = st.columns([2, 1])
with col1:
    st.markdown("""
    ### New Voices Shaping the Narrative of Technology for the Public Interest  
    Emerging leaders in technology are offering diverse perspectives to reshape how society understands the public impact of innovation.  
    Through the Public Voices Fellowship on Technology in the Public Interest, participants receive mentoring and guidance to strengthen their leadership and storytelling.  
    This initiative, supported by the MacArthur Foundation and The OpEd Project, highlights how inclusive voices can shape technology for social good.  
    [Read more →](https://www.macfound.org/press/grantee-news/new-voices-shaping-narrative-of-technology-for-the-public-interest)
    """)
with col2:
    st.markdown(f'<img src="data:image/png;base64,{macfound_b64}" style="width:100%; border-radius:10px;">', unsafe_allow_html=True)

st.markdown("---")

# ---  ---
col1, col2 = st.columns([2, 1])
with col1:
    st.markdown("""
    ### PiTech Fellows in Action: Building Accessible Tech Together  
    At Cornell Tech, the Public Interest Technology (PiTech) Fellowship empowers Ph.D. students to co-create technology alongside communities, not just for them.  
    Fellow Tobias Weinberg’s collaboration with YAI led to new designs in assistive communication that better reflect humor, timing, and human connection.  
    Their work highlights how inclusive partnerships between researchers and nonprofits can transform accessibility into empathy-driven innovation.  
    [Read more →](https://tech.cornell.edu/news/pitech-fellows-yai-tobias-weinberg/)
    """)
with col2:
    st.markdown(f'<img src="data:image/png;base64,{techcornell_b64}" style="width:100%; border-radius:10px;">', unsafe_allow_html=True)

st.markdown("---")

# ---  ---
col1, col2 = st.columns([2, 1])
with col1:
    st.markdown("""
    ### Tech Talks: The Role of Public Interest Technologist in Policy Making  
    The Center for Democracy and Technology’s *Tech Talks* podcast explores how public interest technologists influence digital policy.  
    Experts discuss how their technical expertise shapes decisions on privacy, cybersecurity, and AI governance while keeping human rights at the forefront.  
    The episode highlights why bridging technology and policy is crucial to ensuring innovation serves democracy and the public good.  
    [Read more →](https://cdt.org/insights/tech-talks-the-role-of-public-interest-technologist-in-policy-making/)
    """)
with col2:
    st.markdown(f'<img src="data:image/png;base64,{cdt_b64}" style="width:100%; border-radius:10px;">', unsafe_allow_html=True)

st.markdown("---")

# --- 
col1, col2 = st.columns([2, 1])
with col1:
    st.markdown("""
    ### How Public Interest Technology Is Taking Root on Our Campuses  
    New America’s Public Interest Technology (PIT) initiative is cultivating the next generation of technologists who center equity and ethics in their work.  
    Universities across the United States are embedding PIT into curricula, fostering partnerships between students, governments, and nonprofits.  
    This growing movement ensures technology education equips future leaders to serve communities and strengthen democracy.  
    [Read more →](https://www.newamerica.org/pit/blog/how-public-interest-technology-is-taking-root-on-our-campuses/)
    """)
with col2:
    st.markdown(f'<img src="data:image/png;base64,{napit_b64}" style="width:100%; border-radius:10px;">', unsafe_allow_html=True)

st.markdown("---")
st.caption("© 2025 PIT-NE — Public Interest Technology Network Explorer")
