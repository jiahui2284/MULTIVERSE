from playwright.sync_api import sync_playwright
import csv, time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://alltechishuman.org/responsible-tech-job-board")
    time.sleep(5)   

    
    page.click('#dropdown5 .dropdown-button')
    time.sleep(5)

    search_box = page.query_selector('.dropdown-menu.active input.dropdown-search')
    search_box.focus()
    search_box.type('Cybersecurity', delay=100)
    time.sleep(5)
    page.locator('.dropdown-menu.active >> text="Cybersecurity"').click(force=True)
    time.sleep(5)   

    jobs = []

    while True:
        page.wait_for_selector(".job-card.loading-effect")
                
        cards = page.query_selector_all(".job-card.loading-effect")
        for idx, card in enumerate(cards):
            try:
                title = card.query_selector(".job-title").inner_text().strip()
                fields = card.query_selector_all(".field-div")
                company  = fields[0].inner_text().strip() if len(fields) > 0 else ""
                location = fields[1].inner_text().strip() if len(fields) > 1 else ""
                if "year" in location.lower():
                    location = "Remote"

                card.scroll_into_view_if_needed()
                card.click(force=True)
                time.sleep(3)

       
                job_link = ""
                link_elem = page.query_selector(".apply-div a")
                if link_elem:
                    job_link = link_elem.get_attribute("href")

       
                close_btn = page.query_selector("span.close")
                if close_btn:
                    close_btn.click()
                    time.sleep(1.5)

                jobs.append([title, company, location, job_link])
   

            except Exception as e:
                try:
                    close_btn = page.query_selector("span.close")
                    if close_btn:
                        close_btn.click()
                        time.sleep(1)
                except:
                    pass
                continue

        try:
            next_btn = page.query_selector('text="Next"')
            if next_btn:
                page.wait_for_selector('text="Next"', state='visible', timeout=5000)
                next_btn.click(force=True)
                time.sleep(5)
            else:
                break

        except Exception as e:

            break  

    with open("Alltechjobs2.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Job Title", "Company/Organization", "Location", "Job Link"])
        writer.writerows(jobs)

    print(f"Get jobs.csv , {len(jobs)} jobs。")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass
