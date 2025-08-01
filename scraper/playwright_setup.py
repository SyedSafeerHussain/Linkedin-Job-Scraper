# scraper/playwright_setup.py

from playwright.sync_api import sync_playwright
from utils.session_manager import load_cookie

def launch_browser_with_cookies():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Load cookies
    load_cookie(context)
    page.goto("https://www.linkedin.com/feed/", timeout=60000)

    print("[✓] LinkedIn loaded. Press Enter to continue...")
    input()

    return browser, context, page