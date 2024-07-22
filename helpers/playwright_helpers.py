from playwright.sync_api import Playwright, Browser, BrowserContext

def launch_browser(playwright: Playwright, browser_type: str = 'chromium', headless: bool = True, maximize: bool = False) -> Browser:
    if browser_type == 'chromium':
        browser = playwright.chromium.launch(headless=headless)
    elif browser_type == 'firefox':
        browser = playwright.firefox.launch(headless=headless)
    elif browser_type == 'webkit':
        browser = playwright.webkit.launch(headless=headless)
    else:
        raise ValueError(f"Unsupported browser type: {browser_type}")
    
    if maximize:
        context = browser.new_context(viewport={"width": 1920, "height": 1080})
        
    else:
        context = browser.new_context()

    return context
