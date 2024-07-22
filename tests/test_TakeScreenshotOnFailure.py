import pytest
from playwright.sync_api import sync_playwright
import allure

@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()

def test_example(browser):
    browser.goto("https://example.com")
    assert browser.title() == "Non-existent Title"  # This will fail
