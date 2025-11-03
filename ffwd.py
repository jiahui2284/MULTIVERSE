import time
import pandas as pd
from DrissionPage import ChromiumPage



dp = ChromiumPage()
dp.get('https://jobs.ffwd.org/jobs?filter=eyJzZWFyY2hhYmxlX2xvY2F0aW9ucyI6WyJVbml0ZWQgU3RhdGVzIl19')
dp.wait.doc_loaded()

# wait for the primary page at least appear one jobcard
dp.wait.ele_displayed('css=[data-testid="job-card"], .job-card, [class*="JobCard"]', timeout=10)
load_more = dp.ele('css=button[data-testid="load_more"],button[data-testid="load-more"]', timeout=2)
load_more.click()
def get_doc_height():
    return dp.run_js('return document.body.scrollHeight')

# scroll to bottom, load the jobcard below
last_height = 0
while True:
    dp.run_js('window.scrollTo(0, document.body.scrollHeight - 1500);')
    time.sleep(1.2)
    dp.run_js('window.scrollBy(0, -120);')   
    time.sleep(0.6)
    new_height = get_doc_height()
    if new_height == last_height:
        break
    last_height = new_height

records = []

# use stable picking machine to catch all the jobcard
cards = dp.eles('css=[data-testid="job-card"]') \
     or dp.eles('css=.job-card, [class*="JobCard"], article[class*="job"]')

print(f'Found {len(cards)} cards')

def norm_text(el):
    return (el.text if el else '').strip()

def get_attr(el, name):
    try:
        return el.attr(name) if el else ''
    except:
        return ''

for i, card in enumerate(cards, 1):
    try:
        
        dp.scroll.to_see(card)
        time.sleep(0.05)

        # title & link
        title_el = card.ele('css=[data-testid="job-title-link"]')
        title = norm_text(title_el)
        
        job_url_ele = card.ele('css=a.sc-aXZVg.iTaUL.theme_only')
        link = job_url_ele.attr('href') if job_url_ele else ''

        # Company
        company_el = card.ele('css=[data-testid="link"]')
        company = norm_text(company_el)

        # location
        loc_el = card.ele('css=meta[itemprop="address"]')
        location = loc_el.attr('content') if loc_el else ''


        records.append({
            'Job Title': title,
            'Company': company,
            'Location': location,
            'Job link': link,
        })
        print(f'[{i}] {title} | {company} | {location} |{link}') 
    except Exception as e:
        print(f'[{i}] Error: {e}')

df = pd.DataFrame(records)
df.to_csv('jobs.csv', index=False, encoding='utf-8-sig')

print(f"Already got {len(records)} jobs with description to jobs.csv")
