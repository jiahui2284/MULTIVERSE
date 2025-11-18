from concurrent.futures import ThreadPoolExecutor, as_completed
import time, requests, pandas as pd
from bs4 import BeautifulSoup
import re

# ============================================
# 0. Load dataset
# ============================================
df = pd.read_csv("checked41.csv")

link_column, title_column = "job_link", "job_title"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}



# ============================================
# 1. Domain Classification Keywords
# ============================================
domains = {
    "Policy": ["policy", "public policy", "technology policy", "legislation"],
    "AI Governance": ["ai governance", "algorithmic governance", "ai regulation"],
    "Responsible AI": ["ethical ai", "responsible ai", "ai ethics", "fairness", "bias"],
    "Cybersecurity": ["cybersecurity", "information security", "encryption"],
    "Privacy": ["privacy", "data protection", "gdpr", "personal data"],
    "Data Science": ["data science", "machine learning", "deep learning", "analytics"],
    "Digital Governance": ["digital governance", "platform governance", "govtech"],
    "Civic Tech": ["civic tech", "public interest technology", "tech for good"],
    "Digital Ethics": ["digital ethics", "algorithmic transparency", "trust and safety"],
    "Digital Inclusion": ["digital inclusion", "digital equity", "accessibility"],
    "Human Rights": ["human rights", "civil rights", "freedom online"],
    "Developer": ["developer", "software engineer", "programmer"],
    "Research": ["research", "academic research", "policy research"]
}


def classify_domain_columns(title, text):
    combined = f"{title} {text}".lower()
    result = {}
    found_any = False

    for domain, keywords in domains.items():
        if any(k in combined for k in keywords):
            result[domain] = "yes"
            found_any = True
        else:
            result[domain] = "no"

    result["Other"] = "no" if found_any else "yes"
    return result



# ============================================
# 2. Seniority Classifier v7.0
# ============================================

# --- Title keywords ---
seniority_title_map = {
    "Executive": [
        "founder", "co-founder",
        "chief", "cfo", "ceo", "coo", "cto", "ciso", "cro",
        "president", "vice president", "vp", "svp", "evp",
        "executive director", "managing director",
        "partner", "senior partner"
    ],

    "Director": [
        "director", "associate director", "assistant director",
        "deputy director", "principal director",
        "head of", "head,", "lead of"
    ],

    "Senior Manager": [
        "senior manager", "sr manager",
        "program manager", "project manager",
        "product manager", "policy manager",
        "operations manager", "people manager",
        "team manager", "portfolio manager",
        "supervisor"
    ],

    "Senior IC": [
        "senior engineer", "senior scientist", "senior researcher",
        "senior data scientist", "senior analyst",
        "lead engineer", "lead scientist", "lead researcher",
        "principal investigator", "principal scientist",
        "principal engineer", "staff engineer", "staff scientist",
        "senior associate", "senior specialist",
        "postdoctoral", "postdoc"
    ],

    "Mid": [
        "engineer ii", "engineer iii", "scientist ii", "scientist iii",
        "analyst ii", "analyst iii",
        "associate", "research associate",
        "policy analyst", "data analyst", "research analyst",
        "advisor", "consultant", "officer", "specialist",
        "coordinator", "project coordinator",
        "technician", "technologist"
    ],

    "Entry": [
        "intern", "internship", "trainee", "apprentice",
        "junior", "entry level",
        "assistant", "research assistant",
        "fellow", "graduate fellow",
        "teaching assistant", "lab assistant",
        "student", "recent graduate",
        "early career"
    ]
}

# --- Numeric Level Mapping ---
numeric_seniority = {
    "Executive": [" vi", " vii", " 6", " 7"],
    "Director": [" v", " 5"],
    "Senior IC": [" iv", " 4"],
    "Mid": [" iii", " 3", " ii", " 2"],
    "Entry": [" i", " 1"]
}

# --- Extract experience years ---
def extract_experience(text):
    text = text.lower()

    patterns = [
        (r"(\d+)\s*\+\s*years", lambda x: int(x.group(1))),
        (r"(\d+)\s*-\s*(\d+)\s*years", lambda x: int(x.group(2))),
        (r"minimum of\s*(\d+)\s*years", lambda x: int(x.group(1))),
        (r"at least\s*(\d+)\s*years", lambda x: int(x.group(1))),
        (r"(\d+)\s*years of experience", lambda x: int(x.group(1))),
        (r"(\d+)\s*years", lambda x: int(x.group(1))),
    ]

    for reg, fn in patterns:
        m = re.search(reg, text)
        if m:
            return fn(m)
    return None

# --- Convert years to seniority level ---
def experience_to_level(years):
    if years is None: return None
    if years <= 1: return "Entry"
    if years <= 3: return "Entry"
    if years <= 5: return "Mid"
    if years <= 7: return "Senior IC"
    if years <= 10: return "Senior Manager"
    if years <= 15: return "Director"
    return "Executive"

# --- Final seniority classifier ---
def classify_seniority(title, description_text):
    title_clean = title.lower()

    # Special cases
    if "fellow" in title_clean:
        return "Entry"
    if "postdoc" in title_clean or "postdoctoral" in title_clean:
        return "Senior IC"

    # 1. numeric signals
    for level, tokens in numeric_seniority.items():
        if any(t in title_clean for t in tokens):
            return level

    # 2. title keyword signals
    for level, keywords in seniority_title_map.items():
        if any(k in title_clean for k in keywords):
            return level

    # 3. experience-based
    years = extract_experience(description_text)
    exp_level = experience_to_level(years)
    if exp_level:
        return exp_level

    return "Unknown"



# ============================================
# 3. Fetch job page → classify domain + seniority
# ============================================
def fetch_and_classify(url, title):
    try:
        r = requests.get(url, headers=headers, timeout=12)

        if r.status_code != 200:
            description = ""
        else:
            soup = BeautifulSoup(r.text, "html.parser")
            description = soup.get_text(separator=" ").lower()

            # Improve title if page <title> exists
            if soup.find("title"):
                title = soup.find("title").get_text()

        domain_dict = classify_domain_columns(title, description)
        seniority = classify_seniority(title, description)

        return domain_dict, seniority

    except Exception:
        return classify_domain_columns(title, ""), classify_seniority(title, "")



# ============================================
# 4. Concurrent Processing
# ============================================
start = time.time()
total = len(df)

results_domain = [None] * total
results_seniority = [None] * total

with ThreadPoolExecutor(max_workers=15) as executor:
    futures = {
        executor.submit(fetch_and_classify, row[link_column], row[title_column]): i
        for i, row in df.iterrows()
    }

    for future in as_completed(futures):
        idx = futures[future]
        domain_dict, seniority = future.result()
        results_domain[idx] = domain_dict
        results_seniority[idx] = seniority



# ============================================
# 5. Add Columns & Save
# ============================================
domain_df = pd.DataFrame(results_domain)
df = pd.concat([df, domain_df], axis=1)

df["Seniority"] = results_seniority

df.to_csv("checked5.csv", index=False, encoding="utf-8")

print(f"\n✅ Finished in {(time.time() - start):.2f}s — saved to checked5.csv")