import pandas as pd
import requests
from bs4 import BeautifulSoup
import time, random

df = pd.read_csv("merged_jobs.csv") 
link_column = "job_link"
title_column = "job_title"  
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

keywords = [
    "cybersecurity","governance","ethics","legal","public", 
    "non-profit", "government", "policy", "advocacy", "social", 
    "community", "sustainability","security","protection","welfare",
    "regulation","compliance","outreach","development","funding",
    "grants","volunteer","charity","ngo","non governmental",
    "environmental","humanitarian","civic","inclusion","equity","diversity","privacy",
    "data protection","PIT"
]

def check_keyword(url):
    for attempt in range(2):  
        try:
            response = requests.get(url, headers=headers, timeout=15)
            if response.status_code == 429:
                wait_time = random.uniform(2, 3)
                print(f"⏳ Too many requests, waiting {wait_time:.1f} seconds...")
                time.sleep(wait_time)
                continue
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")
            text = soup.get_text().lower()
            return "yes" if any(k in text for k in keywords) else "no"
        except requests.RequestException as e:
            print(f" Failed to visit ({url}): {e}")
            wait_time = random.uniform(2, 3)
            time.sleep(wait_time)
    return "no"

results = []
for idx, row in df.iterrows():
    job_title = str(row[title_column]).lower()
    url = row[link_column]
    print(f"\n🔍 Checking {idx+1}/{len(df)}: {row[title_column]}")

    if any(k in job_title for k in keywords):
        print("💡 Job title already contains keyword → Mark YES (skip link)")
        result = "yes"
    else:
        print("🌐 Checking job link content...")
        result = check_keyword(url)
        time.sleep(random.uniform(2, 3))

    results.append(result)

df["has_keyword"] = results
df.to_csv("checked.csv", index=False, encoding="utf-8")
print("\n✅ Done! Results saved to checked.csv")

