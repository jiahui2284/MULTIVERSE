from concurrent.futures import ThreadPoolExecutor, as_completed
import time, requests, pandas as pd
from bs4 import BeautifulSoup

# === Load dataset ===
df = pd.read_csv("checked41.csv")

# Update these if your CSV uses different column names
link_column, title_column = "job_link", "company"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

# === Domain classification keywords ===
domains = {
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
    ],
    "Public Interest Technology": [
        "cybersecurity", "privacy", "civic tech", "digital rights",
        "ethics", "accessibility", "public policy", "data justice",
        "open data", "transparency", "digital inclusion"
    ]
}

# === Helper function to classify domain ===
def classify_domain(title, text):
    combined = f"{title} {text}".lower()
    for domain, keywords in domains.items():
        if any(k in combined for k in keywords):
            return domain
    return "Other"

# === Function to fetch page and classify ===
def fetch_and_classify(url, title):
    try:
        r = requests.get(url, headers=headers, timeout=10)
        if r.status_code != 200:
            return classify_domain(title, "")
        soup = BeautifulSoup(r.text, "html.parser")
        text = soup.get_text().lower()
        domain = classify_domain(title, text)
        return domain
    except Exception:
        return classify_domain(title, "")

# === Process each row ===
def process_row(idx, row, total):
    title = str(row[title_column]).lower()
    url = str(row[link_column])
    print(f"🔍 [{idx+1}/{total}] Checking: {row[title_column]}")
    domain = fetch_and_classify(url, title)
    print(f"✅ Done {idx+1}/{total}: Domain={domain}")
    return domain

# === Main concurrent execution ===
start = time.time()
total = len(df)
results_domain = [None]*total

with ThreadPoolExecutor(max_workers=15) as executor:
    futures = {executor.submit(process_row, i, row, total): i for i, row in df.iterrows()}
    for future in as_completed(futures):
        i = futures[future]
        results_domain[i] = future.result()

# === Add Job Domain column ===
df["Job Domain"] = results_domain


# === Save output ===
df.to_csv("checked5.csv", index=False, encoding="utf-8")
print(f"\n✅ Done in {(time.time() - start):.2f}s — Results saved to checked5.csv")
