from concurrent.futures import ThreadPoolExecutor, as_completed
import time, requests, pandas as pd
from bs4 import BeautifulSoup

# === Load dataset ===
df = pd.read_csv("checked41.csv")

link_column, title_column = "job_link", "job_title"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

# === Refined domain keywords ===
domains = {
    "Policy & Governance": [
        "policy", "regulation", "compliance", "oversight", "governance",
        "digital governance", "data governance", "technology governance",
        "platform governance", "public policy", "tech policy", "ai governance",
        "public accountability", "transparency", "open data", "open government",
        "govtech", "digital democracy", "e-government", "digital regulation"
    ],
    "Ethics & Responsible Tech": [
        "ethics", "responsible tech", "responsible technology", "ethical ai",
        "ai ethics", "algorithmic transparency", "algorithmic accountability",
        "algorithmic fairness", "explainable ai", "human-centered",
        "responsible innovation", "value-sensitive design", "trust and safety",
        "ethical computing", "ethical design", "fairness", "ai governance framework"
    ],
    "Cybersecurity & Privacy": [
        "cybersecurity", "cyber security", "security", "data security",
        "privacy", "data protection", "protection", "encryption",
        "resilience", "cyber resilience", "information security", "risk management"
    ],
    "Civic Tech & Social Impact": [
        "civic", "civic tech", "civic engagement", "civic participation",
        "digital rights", "digital inclusion", "digital equity", "digital accessibility",
        "inclusion", "diversity", "equity", "social justice", "social impact",
        "social innovation", "community", "accessibility", "digital wellbeing",
        "civic innovation", "public interest", "technology for good"
    ],
    "Nonprofit & Philanthropy": [
        "non-profit", "nonprofit", "ngo", "charity", "volunteer", "philanthropy",
        "funding", "grants", "impact investing", "social enterprise",
        "sustainability", "environmental", "development", "humanitarian",
        "public service", "welfare", "foundation", "donor"
    ],
    "STEM": [
        "science", "engineer", "developer", "research", "data", "biotech",
        "physics", "chemistry", "mathematics", "ai", "machine learning",
        "software", "hardware", "technical", "scientist"
    ],
    "Arts": [
        "design", "artist", "creative", "curator", "museum", "music", "film",
        "writer", "editor", "photography", "theatre", "painting"
    ],
    "Humanities": [
        "history", "philosophy", "literature", "sociology", "anthropology",
        "language", "culture", "archaeology", "religion", "ethics"
    ]
}

# === Multi-column classifier ===
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

    # Add "Other" column
    result["Other"] = "no" if found_any else "yes"
    return result

# === Fetch & classify ===
def fetch_and_classify(url, title):
    try:
        r = requests.get(url, headers=headers, timeout=10)
        if r.status_code != 200:
            return classify_domain_columns(title, "")
        soup = BeautifulSoup(r.text, "html.parser")
        text = soup.get_text().lower()
        return classify_domain_columns(title, text)
    except Exception:
        return classify_domain_columns(title, "")

# === Process each row ===
def process_row(idx, row, total):
    title = str(row[title_column])
    url = str(row[link_column])
    print(f"🔍 [{idx+1}/{total}] Checking: {title}")
    domain_dict = fetch_and_classify(url, title)
    print(f"✅ Done {idx+1}/{total}")
    return domain_dict

# === Run concurrently ===
start = time.time()
total = len(df)
results = [None] * total

with ThreadPoolExecutor(max_workers=15) as executor:
    futures = {executor.submit(process_row, i, row, total): i for i, row in df.iterrows()}
    for future in as_completed(futures):
        i = futures[future]
        results[i] = future.result()

# === Combine results ===
domain_df = pd.DataFrame(results)
df = pd.concat([df, domain_df], axis=1)

# === Save ===
df.to_csv("checked5.csv", index=False, encoding="utf-8")
print(f"\n✅ Done in {(time.time() - start):.2f}s — Results saved to checked5.csv")
