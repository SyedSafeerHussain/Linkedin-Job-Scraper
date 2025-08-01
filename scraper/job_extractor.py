# scraper/job_extractor.py

from playwright.sync_api import Page
import time

def extract_jobs(page: Page, num_scrolls: int = 3) -> list:
    jobs = []

    for _ in range(num_scrolls):
        page.mouse.wheel(0, 2000)
        time.sleep(2)

    job_cards = page.query_selector_all("div.ember-view")

    for job in job_cards:
        title_elem = job.query_selector("strong")
        company_elem = job.query_selector("div.artdeco-entity-lockup__subtitle")
        location_elem = job.query_selector("div.artdeco-entity-lockup__caption")

        if title_elem and company_elem and location_elem:
            jobs.append({
                "title": title_elem.inner_text().strip(),
                "company": company_elem.inner_text().strip(),
                "location": location_elem.inner_text().strip()
            })

    return jobs
