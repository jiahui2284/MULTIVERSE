from concurrent.futures import ThreadPoolExecutor, as_completed
import time, requests, pandas as pd
from bs4 import BeautifulSoup

df = pd.read_csv("merged.csv")
link_column, title_column = "job_link", "job_title"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
keywords = [
    "public interest technology", "public interest tech", "PIT", "PITeN", "public interest",
    "tech for good", "technology for good", "social impact", "social innovation",
    "cybersecurity", "security", "protection", "privacy", "data protection", "data ethics", "responsible tech",
    "responsible technology", "ethical AI", "AI ethics", "tech for good", "tech policy", "tech law",
    "civil rights", "citizen", "public interest", "public service", "public policy", "public technology",
    "digital rights", "digital wellbeing", "digital well-being", "digital inclusion", "digital equity",
    "digital accessibility", "accessibility", "inclusion", "diversity", "equity", "social justice",
    "social impact", "social innovation", "social responsibility", "social good", "community",
    "community engagement", "community empowerment", "community technology", "civic", "civic tech",
    "civic engagement", "civic participation", "civic technology", "civic innovation",

    "governance", "digital governance", "internet governance", "data governance", "technology governance",
    "AI governance", "public accountability", "public transparency", "policy", "regulation",
    "compliance", "oversight", "technology regulation", "digital regulation", "tech accountability",
    "policy innovation", "participatory governance", "digital democracy", "e-government", "open government",
    "open data", "GovTech", "public sector innovation", "technology oversight", "technology and democracy",

    "ethics", "technology ethics", "digital ethics", "algorithmic accountability", "algorithmic transparency",
    "algorithmic bias", "automated decision-making", "AI transparency", "explainable AI",
    "fairness in AI", "ethical design", "ethical innovation", "human-centered technology",
    "value-sensitive design", "responsible innovation", "trust and safety", "ethical computing",
    "AI governance framework", "human-centered AI", "tech transparency", "risk assessment",

    "information integrity", "disinformation", "misinformation", "fake news", "online safety",
    "cyber resilience", "surveillance", "platform governance", "platform accountability",
    "content moderation", "online moderation", "digital safety", "media literacy", "digital citizenship",
    "freedom of expression", "internet freedom", "human rights online", "data rights", "digital trust",

    "non-profit", "ngo", "non governmental", "charity", "volunteer", "funding", "grants", "philanthropy",
    "digital philanthropy", "tech philanthropy", "impact investing", "social enterprise",
    "philanthropic technology", "nonprofit innovation", "cross-sector collaboration",
    "multi-stakeholder governance", "public-private partnership", "outreach", "development",
    "sustainability", "environmental", "humanitarian", "welfare", "PIT", "tech justice",
    "technology for humanity", "technology for justice", "underserved communities",
    "marginalized groups", "technology for inclusion", "digital commons", "open source for good",
    "digital ethics education", "tech for democracy", "tech stewardship", "public interest research"
]

def check_keyword(url):
    try:
        r = requests.get(url, headers=headers, timeout=10)
        if r.status_code != 200:
            return "no"
        text = BeautifulSoup(r.text, "html.parser").get_text().lower()
        return "yes" if any(k in text for k in keywords) else "no"
    except Exception:
        return "no"

def process_row(idx, row, total):
    title = str(row[title_column]).lower()
    url = row[link_column]
    print(f"🔍 [{idx+1}/{total}] Checking: {row[title_column]}")
    if any(k in title for k in keywords):
        print("💡 Title matched → YES (skip link)")
        return "yes"
    result = check_keyword(url)
    print(f"✅ Done {idx+1}/{total}: {result}")
    return result

start = time.time()
total = len(df)
results = [None] * total

with ThreadPoolExecutor(max_workers=10) as executor:
    futures = {executor.submit(process_row, i, row, total): i for i, row in df.iterrows()}
    for future in as_completed(futures):
        i = futures[future]
        results[i] = future.result()

df["has_keyword"] = results
df.to_csv("checked.csv", index=False, encoding="utf-8")
print(f"\n✅ Done in {(time.time() - start):.2f}s")
