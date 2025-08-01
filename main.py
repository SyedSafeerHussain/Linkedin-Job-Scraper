# main.py

from scraper.playwright_setup import launch_browser_with_cookies
from scraper.job_extractor import extract_jobs
from utils.csv_writer import save_to_csv

def main():
    browser, context, page = launch_browser_with_cookies()

    try:
        search_url = "https://www.linkedin.com/jobs/search/?keywords=python%20developer"
        page.goto(search_url, timeout=60000)
        page.wait_for_timeout(5000)

        jobs = extract_jobs(page)
        save_to_csv(jobs, "data/jobs.csv")

        print(f"✅ Extracted and saved {len(jobs)} jobs to data/jobs.csv")

    finally:
        browser.close()

if __name__ == "__main__":
    main()
