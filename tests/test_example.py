import pytest
from playwright.sync_api import sync_playwright
from helpers.playwright_helpers import launch_browser
def test_google_search():
   with sync_playwright() as p:
        # Launch browser using custom helper function
        browser = launch_browser(p, browser_type='firefox', headless=False, maximize=True)
       
        page = browser.new_page()
         # Maximize the browser window using the helper function
        
        # Go to Google search page
        page.goto("https://www.google.com")
        
        # Perform search
        page.fill('textarea[name="q"]', 'Playwright')
        page.press('input[name="btnK"]', 'Enter')
        
        # Wait for results to load
        page.wait_for_load_state('networkidle')
        
        # Assert that results contain "Playwright"
        assert "Playwright" in page.content()
        
        # Close browser after some delay to observe results
        page.wait_for_timeout(5000)
        
        #context.close()
        browser.close()
        
if __name__ == "__main__":
    pytest.main(["-v", f"--html=reports/report.html"])

