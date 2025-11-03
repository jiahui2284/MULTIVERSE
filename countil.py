import time
import pandas as pd
from DrissionPage import ChromiumPage

dp = ChromiumPage()
url = "https://careers.councilofnonprofits.org/search/#results/6906494386c2e8da426255c8?page_num=1&kw="
dp.get(url)
dp.wait.ele_displayed('css=col-md-9', timeout=5)

records = []
def get_current_page():
    el = dp.ele('css=li.page.active a')
    return int(el.attr('data-page')) if el else 1

# 🔹Scrape to get the max visible page
def get_last_page_visible():
    els = dp.eles('css=li.page a[data-page]')
    nums = []
    for a in els:
        t = a.attr('data-page')
        if t and t.isdigit():
            nums.append(int(t))
    return max(nums) if nums else 1
page_num = get_current_page()
last_num  = get_last_page_visible()
print(f'📄 Current page: {page_num} / Overall page: {last_num}')

while True:
    print(f"\n🌍 Scraping page {page_num} ...")

    # Get job cards
    cards = dp.eles('css=li.cl-job')
    print(f"📦 Found {len(cards)} job cards on this page.")

    for i, card in enumerate(cards, 1):
        try:
            dp.scroll.to_see(card)
            time.sleep(0.05)

            title_el = card.ele('css=h2')
            company_el = card.ele('css=span.cl-job-company')
            loc_el = card.eles('css=span.cl-job-location')
            link_el = card.ele('css=a.cl-job-link')

            title = title_el.text.strip() if title_el else ''
            company = company_el.text.strip() if company_el else ''
            if len(loc_el) >= 2:
                location = loc_el[-1].text.strip()
            elif loc_el:
                location = loc_el[0].text.strip()
            else:
                location = ''

            link = link_el.attr('href') if link_el else ''


            records.append({
                'Job Title': title,
                'Company': company,
                'Location': location,
                'Job link': link
            })

            print(f"[{i}] {title} | {company} | {location} | {link}")

        except Exception as e:
            print(f"[{i}] Error: {e}")

    # Is it already scroll to the last page
    page_num = get_current_page()
    last_num = get_last_page_visible()
    print(f"📄 processing: {page_num}/{last_num}")
    if page_num >= last_num:
        print("✅ already scroll to the last page，stop。")
        break

    # flip to next page control
    next_num = page_num + 1
    next_link = dp.ele(f'css=li.page a[data-page="{next_num}"]')

    if not next_link:
        print("✅ no more next page button，end。")
        break

    dp.scroll.to_see(next_link)
    print(f"➡️ press the page {next_num} ...")
    next_link.click()
    page_num += 1

    # wait for the new page loading, detect the page change
    for _ in range(30):
        time.sleep(0.5)
        now = get_current_page()
        if now == next_num:
            break
    else:
        print("⚠️ page never update, avoid to get in for loop forever, stop")
        break

# remove duplicate and save
df = pd.DataFrame(records)
df.drop_duplicates(subset=['Job Title', 'Company', 'Location', 'Job link'], inplace=True)
df.to_csv('council_jobs.csv', index=False, encoding='utf-8-sig')
print(f"\n✅ Done! {len(df)} jobs scraped and saved as council_jobs.csv")