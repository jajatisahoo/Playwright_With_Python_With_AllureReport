import pytest
import allure
from playwright.sync_api import sync_playwright
@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {
            "width": 1920,
            "height": 1080,
            
        }
    }
    
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # Execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    print("Hello world")
    # Check if the test failed
    if rep.when == 'call' and rep.failed:
        # Take a screenshot if the test failed
        page = item.funcargs.get('browser')
        if page:
            screenshot = page.screenshot(path=f"screenshots/{item.name}.png")
            allure.attach.file(f"screenshots/{item.name}.png", name=f"{item.name} Screenshot", attachment_type=allure.attachment_type.PNG)    