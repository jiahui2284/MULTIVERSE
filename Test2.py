import time
import pandas as pd
from DrissionPage import ChromiumPage, ChromiumOptions

co = ChromiumOptions()
co.headless(True)
dp = ChromiumPage(co)

base_url = 'https://aijobs.ai/united-states'

records = []

def scrape_jobs():
    job_cards = dp.eles('css=.col-xl-4.col-md-6')
    count = 0
    for card in job_cards:
        try:
            a_tag = card.ele('css=a')
            job_link = a_tag.attr('href') if a_tag else ''

            title_ele = card.ele('css=.tw-text-lg.tw-font-medium')
            job_title = title_ele.text.strip() if title_ele else ''

            company_ele = card.ele('css=.tw-card-title')
            company = company_ele.text.strip() if company_ele else ''

            loc_ele = card.ele('css=.tw-location')
            location = loc_ele.text.strip() if loc_ele else ''

            records.append({
                'Job Title': job_title,
                'Company': company,
                'Location': location,
                'Job link': job_link
            })
            count += 1
        except:
            continue
    return count

page = 1
max_empty_pages = 2  
empty_count = 0

while True:
    url = f"{base_url}?page={page}"
    dp.get(url)
    dp.wait.doc_loaded()
    time.sleep(2)

    count = scrape_jobs()
    print(f"📄 Page {page} → {count} jobs")

    
    if count == 0:
        empty_count += 1
        if empty_count >= max_empty_pages:
            print("🚫 No more pages, stopping.")
            break
    else:
        empty_count = 0  
    
    page += 1

dp.quit()

df = pd.DataFrame(records)
df.drop_duplicates(subset=['Job Title', 'Company'], inplace=True)
df.to_csv('aijobs_ai_US.csv', index=False, encoding='utf-8-sig')

print(f"\n get {len(df)} jobs, aijobs_ai_US.csv")
