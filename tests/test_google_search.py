import pytest
from playwright.sync_api import sync_playwright
from pages.base_page import BasePage
from helpers.playwright_helpers import launch_browser

@pytest.mark.not_consider
def test_google_search():
    with sync_playwright() as p:
         # Launch browser using custom helper function
        browser = launch_browser(p, browser_type='firefox', headless=False, maximize=True)
       
        page = browser.new_page()
        base_page = BasePage(page)
        
        # Navigate to Google
        base_page.goto("https://www.google.com")
        
        # Perform search
        base_page.fill_input('textarea[name="q"]', 'Playwright')
        base_page.click_button('input[name="btnK1"]')
        assert browser.title() == "Non-existent Title"  # This will fail
        
        # Wait for results to load
        base_page.wait_for_selector('div#search')
        
        # Assert that results contain "Playwright"
        assert "Playwright" in base_page.get_page_content()
        
        # Close browser after some delay to observe results
        page.wait_for_timeout(5000)

if __name__ == "__main__":
    pytest.main(["-v", f"--html=reports/report.html"])
