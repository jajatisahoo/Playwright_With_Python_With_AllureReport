import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage

@pytest.fixture(scope="module")

def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        yield browser
        browser.close()
@pytest.mark.not_consider
def test_login_with_invalid_credentials(browser):
    page = browser.new_page()
    login_page = LoginPage(page)
    login_page.load()

    login_page.set_username("invalid_username")
    login_page.set_password("invalid_password")
    login_page.click_login_button()

    error_message = login_page.get_error_message()
    assert "Invalid credentials" in error_message

    page.close()
