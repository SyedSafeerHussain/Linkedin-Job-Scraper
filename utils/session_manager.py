import json
from playwright.sync_api import BrowserContext
def load_cookie(context: BrowserContext, cookie_file_path: str="data/cookies.json"):
    """Load cookies from JSON file into the current browser context."""
    try:
        with open(cookie_file_path,'r')as f:
            cookies=json.load(f)
        context.add_cookies(cookies)
        print("[✓] Session cookies loaded successfully.")
    except Exception as e:
        print(f"[!] Failed to load cookies: {e}")

