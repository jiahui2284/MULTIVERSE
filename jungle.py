import time
import pandas as pd
from DrissionPage import ChromiumPage



dp = ChromiumPage()
url = ('https://www.welcometothejungle.com/en/jobs?aroundQuery=United%20States&query=&refinementList%5Boffices.country_code%5D%5B%5D=US&page=1&searchTitle=true')
dp.get(url)
dp.wait.ele_displayed('css=li[data-testid="search-results-list-item-wrapper"]', timeout=1)

records = []

def get_current_page():
    el = dp.ele('xpath=//nav[@aria-label="Pagination"]//a[@aria-current="true"]')
    return int(el.text.strip()) if el else 1

def get_last_page_visible():
    els = dp.eles('xpath=//nav[@aria-label="Pagination"]//a[@aria-current]')
    nums = []
    for a in els:
        t = (a.text or '').strip()
        if t.isdigit():
            nums.append(int(t))
    return max(nums) if nums else 1

page_num = get_current_page()
last_num  = get_last_page_visible()
print(f'📄 Current page: {page_num} / Overall page: {last_num}')

while True:
    print(f"\n🌍 scrape the {page_num} page ...")

    # 抓取当页
    cards = dp.eles('css=li[data-testid="search-results-list-item-wrapper"]')
    print(f"📦 This page has {len(cards)} jobs")
    for i, card in enumerate(cards, 1):
        try:
            dp.scroll.to_see(card); time.sleep(0.03)
            title_el = card.ele('css=h2[class*="sc-izXThL"][class*="wui-text"] div[role="mark"]')
            company_el = card.ele('css=span[class*="wui-text"]')
            loc_el = card.ele('css=span[class*="sc-hzawhJ"]')
            link_el = card.ele('css=a[role="link"][href*="/en/companies/"]')

            title = (title_el.text or '').strip() if title_el else ''
            company = (company_el.text or '').strip() if company_el else ''
            location = (loc_el.text or '').strip() if loc_el else ''
            link = link_el.attr('href') if link_el else ''
            if link.startswith('/'):
                link = 'https://www.welcometothejungle.com' + link

            records.append({
                'Job Title': title,
                'Company': company,
                'Location': location,
                'Job link': link
            })
        except Exception as e:
            print(f"[{i}] Error: {e}")

    # Is it already scroll to the last page
    page_num = get_current_page()
    last_num = get_last_page_visible()
    print(f"📄 processing: {page_num}/{last_num}")
    if page_num >= last_num:
        print("✅ already scroll to the last page，stop。")
        break

    # press "next page number（current page +1）
    next_num = page_num + 1
    next_link = dp.ele(
        f'xpath=//nav[@aria-label="Pagination"]//a[@aria-current="false" and normalize-space()="{next_num}"]'
    )
    if not next_link:

        next_link = dp.ele('xpath=//nav[@aria-label="Pagination"]//a[normalize-space()="›"]')
    if not next_link:
        print("✅ can not find next page，stop。"); break

    dp.scroll.to_see(next_link); next_link.click()

    # wait the page number really turn to next_num
    for _ in range(30):  # ~15s
        time.sleep(0.5)
        now = get_current_page()
        if now == next_num:
            break
    else:
        print("⚠️ page never update，stop to avoid for loop forever")
        break

# remove duplicate and save
df = pd.DataFrame(records)
df.drop_duplicates(subset=['Job Title', 'Company', 'Location', 'Job link'], inplace=True)
df.to_csv('jobs_jungle_all_pages.csv', index=False, encoding='utf-8-sig')
print(f"\n✅ finish，overall are {len(df)} jobs（after remove duplicate），and save jobs_jungle_all_pages.csv")

