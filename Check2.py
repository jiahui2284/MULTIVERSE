from concurrent.futures import ThreadPoolExecutor, as_completed
import time, requests, pandas as pd
from bs4 import BeautifulSoup

df = pd.read_csv("checked0.csv")
link_column, title_column = "job_link","location"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
keywords = [
    "remote"
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

with ThreadPoolExecutor(max_workers=15) as executor:
    futures = {executor.submit(process_row, i, row, total): i for i, row in df.iterrows()}
    for future in as_completed(futures):
        i = futures[future]
        results[i] = future.result()

df["Remote or Not"] = results
df.to_csv("checked2.csv", index=False, encoding="utf-8")
print(f"\n✅ Done in {(time.time() - start):.2f}s")