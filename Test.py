import time
import pandas as pd
from DrissionPage import ChromiumPage
from DrissionPage import ChromiumOptions

# use this for set the path        
# path = r"C:\Program Files\Google\Chrome\Application\chrome.exe" 
# ChromiumOptions.set_chromium_path(path).(save) 

co = ChromiumOptions()
co.headless(True)

dp = ChromiumPage(co)
dp.get('https://jobs.80000hours.org/?jobPk=17569&refinementList%5Btags_area%5D%5B0%5D=AI%20safety%20%26%20policy&refinementList%5Btags_area%5D%5B1%5D=Global%20health%20%26%20development&refinementList%5Btags_area%5D%5B2%5D=Other%20policy-focused&refinementList%5Btags_location_80k%5D%5B0%5D=USA')
dp.wait.doc_loaded()
# just for 80000 hours jobs page
#loop to scroll to the bottom of the page for loading all job cards
def get_doc_height():
    return dp.run_js('return document.body.scrollHeight')

last_height = 0
while True:
    dp.run_js('window.scrollTo(0, document.body.scrollHeight - 1500);')
    time.sleep(2)
    dp.run_js('window.scrollBy(0, -100);')
    time.sleep(1)
    new_height = get_doc_height()
    if new_height == last_height:
        break
    last_height = new_height

records = []

# get job cards count
total = len(dp.eles('css=.job-card'))

for i in range(total):
    try:
        # get all job cards list
        divs = dp.eles('css=.job-card')
        div = divs[i]

        # make sure the job card is in view
        dp.scroll.to_see(div)
        time.sleep(0.5)

        # expand the job card to see the full description
        div.click()
        time.sleep(1)  

        # get job title and company and location (based on class elements)
        title = ', '.join(j.text.strip() for j in div.eles('css=[class~="font-bold"]') if j.text.strip())
        company = ', '.join(c.text.strip() for c in div.eles('css=[class~="text-sm"][class~="lg:text-base"]') if c.text.strip())
        Loc = div.eles('css=[class*="md:whitespace-normal"]')

        locations = []
        seen = set() # To avoid duplicate locations (We use a set to track seen locations)
        for L in Loc:            #Extract and clean text from sub-elements
            t = L.text.strip()
            if t and t not in seen:
                seen.add(t)
                locations.append(t)
        location = ', '.join(locations)

        # get job description
        desc_ele = div.ele('css=.html-text')
        description = desc_ele.text.strip() if desc_ele else ''

        job_url_ele = div.ele('css=a.view-details-button')
        job_url = job_url_ele.attr('href') if job_url_ele else ''

        records.append({
            'Job Title': title,
            'Company': company,
            'Location': location,
            'Job Description': description,
            'Job link': job_url
        })
        print(f"[{i+1}] {title} ")
    except Exception as e:
        print(f"[{i+1}] Error: {e}")


df = pd.DataFrame(records)
df.to_csv('jobs_80000hours.csv', index=False, encoding='utf-8-sig')

print(" Already got {len(records)} jobs with description to jobs_80000hours.csv")
