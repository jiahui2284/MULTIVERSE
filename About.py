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

# ========= Page Config =========
st.set_page_config(
    page_title="About PIT-NE",
    page_icon="PIT-NE logo.png",  # use main logo file as page icon
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
            <a class="active" href="#" target="_self">About</a>
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
    **Public Interest Technology (PIT)** is a movement at the intersection of **technology, ethics, policy, and social good**.  
    It focuses on designing, developing, and applying technology in ways that **advance equity, justice, accessibility, and democracy** — ensuring that innovation serves communities, not just commercial interests.  
    
    PIT practitioners come from diverse fields — computer science, design, public policy, law, and social sciences — and work on challenges such as:
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
    **PIT-NE (Public Interest Technology New England)** is a regional initiative dedicated to **empowering individuals and organizations across the Northeast U.S.**  

    Our mission is to:
    - 🌱 **Cultivate** a diverse community of technologists committed to social good  
    - 🤝 **Connect** academia, government, nonprofits, and industry to co-create public interest technology projects  
    - 🧭 **Guide** students and professionals toward impactful, socially responsible tech career paths  
    
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
- 🏛️ Integrate ethics and social impact into tech education  
- 💬 Facilitate collaboration between civic organizations and technologists  
- 🔍 Amplify stories of people creating technology for the public good  
- 🌎 Build a sustainable network that nurtures next-generation PIT leaders  
""")

st.markdown("---")

# ========= Section: Project Background =========
st.markdown("## 📘 Project Background")

st.write("""
This PIT-NE prototype website was created as part of **CDS DS 539 – Data Science Practicum** at **Boston University**,  
a project-based course offered through **BU Spark!**.  

In this practicum, our team explored how **data science, visualization, and interactive tools** can help people in  
New England discover opportunities in **Public Interest Technology (PIT)** — especially roles that connect technical skills  
with ethics, policy, and social impact.  
""")

st.markdown("### ❗ The Problem We Saw")

st.write("""
Despite growing interest in **Public Interest Technology**, many people still face challenges when trying to  
understand or enter this field:

- Information about PIT-related jobs and opportunities is **fragmented** across multiple platforms and organizations  
- Job titles and descriptions often use **inconsistent language**, making it difficult to identify roles that truly align  
  with public-interest values (equity, justice, democracy, accessibility, etc.)  
- Students and early-career professionals who care about **social impact** may not know  
  how their **data science or technical skills** connect to PIT careers  

As a result, people who want to work at the intersection of **technology and public good** often lack a clear,  
**welcoming entry point** into the ecosystem.
""")

st.markdown("### 💭 Our Approach & Design Principles")

st.write("""
This project is our attempt to design such an entry point.

Our goals and design principles include:

- 💬 **Make PIT more discoverable**  
  Provide a structured way to explore roles and stories related to Public Interest Technology in the New England region.  

- 🧠 **Translate complexity into clarity**  
  Use simple language, clear categories, and interactive views so that people can quickly understand what a job or field  
  is about — not just read a long description.  

- 🧭 **Center values, not just skills**  
  Highlight how roles relate to **equity, democracy, accessibility, and accountability**, not only programming languages  
  or tools.  

- 🤝 **Bridge data and people**  
  Use data science to organize and filter information, while still keeping the focus on **humans, communities,  
  and public impact**.  

This website is an early prototype, but it reflects our belief that **data science can support more just and  
responsible technology ecosystems**.
""")

st.markdown("---")

# ========= Section: Data & Methodology =========
st.markdown("## 🛠 Data & Methodology")

st.write("""
To build the **PIT-NE Job Explorer**, we collected job postings from public job boards and organization career sites across the New England region.  
Our process involved three main phases: **loading**, **extracting**, and **classifying** the data.
""")

st.markdown("### 1️⃣ How We Collected the Data")

st.write("""
Because different job boards have different structures and often rely on dynamic front-end rendering,  
we used **browser automation tools** rather than only downloading static HTML.

We:

- Inspected the structure of each job site using browser developer tools  
  to locate the HTML elements that contain job titles, organizations, locations, and application links  
- Used a **Chromium-based automation tool** to open job pages programmatically  
- Waited for job cards to fully render in the browser  
- Triggered “load more” buttons when necessary  
- Scrolled dynamically so that lazy-loaded content became visible  
- Selected job-card elements via CSS selectors and extracted relevant text fields  

All collected information — such as job title, employer, location, and job link — was saved into a unified CSV file  
for cleaning, filtering, and analysis.
""")

st.markdown("### 2️⃣ How We Identified PIT-Related Roles")

st.write("""
Not every technical or policy job qualifies as **Public Interest Technology**.  
To focus on PIT-related opportunities, we used a **keyword-based filtering approach** applied to job titles and, when available, descriptions.

Our scripts:

- Maintain a curated list of **PIT-aligned keywords**  
  (for example, keywords related to accessibility, equity, democracy, privacy, civic technology, and public policy)  
- Scan each posting for these keywords  
- Flag roles that match one or more PIT indicators  
- Add structured fields such as:  
  - **Location Type**  
  - **Employer Type**  
  - **Seniority Level**  
  - **Jod domain**  

This method provides a transparent and adaptable way to surface jobs that align with public-interest values.
""")

st.markdown("### 3️⃣ How Others Can Reuse or Extend Our Scripts")

st.write("""
We designed our workflow so that it can be reused and extended by others who are interested in similar questions.

In general, a user can:

- Replace the list of job-board URLs to target different sectors or regions  
- Adjust CSS selectors to match the HTML structure of new sites  
- Modify the PIT keyword list to reflect their own priorities  
  (for example, climate justice, digital rights, or AI safety)  
- Regenerate a dataset and plug it into this Streamlit app to explore new sets of roles  

Our goal is to provide a reusable, extensible pipeline that helps highlight **mission-driven technology opportunities**  
in different communities.
""")

st.markdown("---")

# ========= Section: Our Team =========
st.markdown("## 👥 Our Team")

st.write("""
This project was developed by a team of **Data Science students** at **Boston University** in **CDS DS 539 – Data Science Practicum**:

- **Jiahui Liang** — Data Science  
- **Baijie Li** — Data Science  
- **Hannah Choe** — Data Science  
- **Ryan Cheng** — Data Science  

We are interested in how data, design, policy, and technology can work together to:
- make public interest technology opportunities more visible, and  
- help people navigate careers that align with **impact, responsibility, and equity**.  
""")

st.markdown("---")

# ========= Section: Logo & Identity =========
st.markdown("## 🧭 Our Identity")

col1, col2 = st.columns([2, 1])
with col1:
    st.write("""
    The **PIT-NE** identity brings together both **regional roots** and **digital innovation**.  
    The project focuses on the **New England** region — a hub of universities, civic innovation,  
    and public policy leadership — while highlighting a commitment to technologies that serve the public good.  
    
    Together, these elements represent a vision of **technology that empowers communities and strengthens democracy**.
    """)
with col2:
    # intentionally left blank; no image shown in this section
    pass

st.markdown("---")
st.caption("© 2025 PIT-NE — Public Interest Technology New England.")

