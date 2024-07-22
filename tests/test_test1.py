import re
import pytest
from playwright.sync_api import Page, expect,sync_playwright
from helpers.playwright_helpers import launch_browser
def test_has_title():
    with sync_playwright() as p:
        # Launch browser using custom helper function
        browser = launch_browser(p, browser_type='chromium', headless=False, maximize=True)
        page = browser.new_page()
        page.goto("https://playwright.dev/")

        # Expect a title "to contain" a substring.
        expect(page).to_have_title(re.compile("Playwright"))
@pytest.mark.only_browser("firefox")
def test_get_started_link():
    with sync_playwright() as p:
        # Launch browser using custom helper function
        browser = launch_browser(p, browser_type='chromium', headless=False, maximize=True)
        page = browser.new_page()
        page.goto("https://playwright.dev/")

    # Click the get started link.
        page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
        expect(page.get_by_role("heading", name="Installation")).to_be_visible()
      #context.close()
        browser.close()
        
if __name__ == "__main__":
    pytest.main(["-v", f"--html=reports/report.html"])