import streamlit as st
import base64
import os

# ========= Helper =========
def image_to_base64(path):
    if not os.path.exists(path):
        return ""
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# ========= Load Images =========
logo_base64 = image_to_base64("PIT-NE logo.png")
friendly_base64 = image_to_base64("Friendly.png")
circle_base64 = image_to_base64("fcbf0318-09e8-479c-b95d-598f59234631.png")
Second_logo_base64 = image_to_base64("PITLogo.png")

# ========= Page Config =========
st.set_page_config(
    page_title="About PIT-NE",
    page_icon="PITLogo.png",
    layout="wide",
)

# ========= Navigation =========
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
        padding: 0.4rem 0.8rem;
        border-radius: 8px;
        transition: all 0.2s ease-in-out;
    }}
    .nav-right a:hover {{
        background-color: #004aad;
        color: white;
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
            <div class="nav-title">PIT-NE — About Us</div>
        </div>
        <div class="nav-right">
            <a href="https://multiverse-fsbeuhmjvnyfbdzyhbaemt.streamlit.app/" target="_blank">🏠 Home</a>
            <a class="active" href="#" target="_self">About Us</a>
            <a href="https://multiverse-w9fva7qcna2joe224ixqbe.streamlit.app/" target="_blank">Explore Jobs</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ========= Section: Introduction =========
st.markdown("## 🌍 What Is Public Interest Technology (PIT)?")

col1, col2 = st.columns([2, 1])
with col1:
    st.write("""
    **Public Interest Technology (PIT)** is a movement at the intersection of **technology, ethics, and social good**.  
    It is about designing, developing, and applying technology in ways that **advance equity, justice, and democracy** — ensuring that innovation serves people, not just profit.  
    
    PIT practitioners come from all backgrounds — computer science, policy, law, social sciences, design — working together to solve real-world problems like:
    - Building responsible and fair AI systems  
    - Enhancing digital privacy and trust  
    - Ensuring access and accessibility in technology  
    - Protecting democracy from digital threats  
    """)
with col2:
    if circle_base64:
        st.image(f"data:image/png;base64,{circle_base64}", use_container_width=True)

st.markdown("---")

# ========= Section: Our Mission =========
st.markdown("## 💡 Why PIT-NE Exists")

col1, col2 = st.columns([1, 2])
with col1:
    if friendly_base64:
        st.image(f"data:image/png;base64,{friendly_base64}", use_container_width=True)
with col2:
    st.write("""
    **PIT-NE (Public Interest Technology Network Explorer)** is a regional initiative dedicated to **empowering individuals and organizations across the Northeast U.S.**  
    Our mission is to:
    - 🌱 **Cultivate** a diverse community of technologists committed to social good.  
    - 🤝 **Connect** academia, government, nonprofits, and industry to co-create public interest technology projects.  
    - 🧭 **Guide** professionals and students toward impactful career paths in responsible tech.  
    
    We believe technology should be a **tool for empowerment**, not exploitation.  
    By bridging disciplines and institutions, PIT-NE helps ensure that innovation strengthens — rather than undermines — our shared public values.
    """)

st.markdown("---")

# ========= Section: Our Purpose =========
st.markdown("## 🎯 Our Purpose & Vision")

st.write("""
We envision a future where technology is **deeply aligned with human values** — where design, policy, and innovation  
are all guided by **empathy, accountability, and inclusion**.  

Through partnerships and education, PIT-NE aims to:
- 🏛️ Integrate ethics and social impact into tech education.  
- 💬 Facilitate collaboration between civic organizations and technologists.  
- 🔍 Amplify stories of people creating technology for the public good.  
- 🌎 Build a sustainable network that nurtures next-generation PIT leaders.  
""")

st.markdown("---")

# ========= Section: Logo & Identity =========
st.markdown("## 🧭 Our Identity")

col1, col2 = st.columns([2, 1])
with col1:
    st.write("""
    The **PIT-NE** logo represents both **regional roots** and **digital innovation**.  
    The map outline reflects the Northeastern United States — a hub of universities, civic innovation,  
    and public policy leadership — while the circuitry pattern symbolizes our connection between technology and humanity.  
    
    Together, these elements stand for a shared vision:  
    using technology not for domination, but for **democratic empowerment and equity**.
    """)
with col2:
    if logo_base64:
        st.image(f"data:image/png;base64,{Second_logo_base64}", use_container_width=True)

st.markdown("---")
st.caption("© 2025 PIT-NE — Public Interest Technology Network Explorer")

