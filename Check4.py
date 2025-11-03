from concurrent.futures import ThreadPoolExecutor, as_completed
import time, requests, pandas as pd
from bs4 import BeautifulSoup

# 输入与输出文件
df = pd.read_csv("checked3.csv")
link_column = "job_link"

# 新关键字（检测坏链）
keywords = ["error", "404", "can't open","not found", "page missing","page cannot be found","page you were looking for doesn't exist"
            ,"the requested URL was not found on this server","we can't find the page you're looking for"
            ,"the page you requested could not be found","the page cannot be found","sorry, we couldn't find that page"
            ,"the page you are looking for might have been removed","the page has been moved or deleted"
            ,"this page is no longer available","the link you followed may be broken or expired"
            ,"we're sorry, but the page you requested could not be found"
            ,"404 not found","page not found","webpage not available","page is unavailable","page is not available"
            ]

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

def check_keyword(url):
    try:
        r = requests.get(url, headers=headers, timeout=10)
        if r.status_code != 200:
            return "missing"
        text = BeautifulSoup(r.text, "html.parser").get_text().lower()
        return "missing" if any(k in text for k in keywords) else "ok"
    except Exception:
        return "missing"

def process_row(idx, row, total):
    url = row[link_column]
    print(f"🔍 [{idx+1}/{total}] Checking: {url}")
    result = check_keyword(url)
    print(f" Done {idx+1}/{total}: {result}")
    return result

start = time.time()
total = len(df)
results = [None] * total

with ThreadPoolExecutor(max_workers=15) as executor:
    futures = {executor.submit(process_row, i, row, total): i for i, row in df.iterrows()}
    for future in as_completed(futures):
        i = futures[future]
        results[i] = future.result()

df["Missing Link"] = results
df.to_csv("checked4.csv", index=False, encoding="utf-8")
print(f"\n Done in {(time.time() - start):.2f}s")
