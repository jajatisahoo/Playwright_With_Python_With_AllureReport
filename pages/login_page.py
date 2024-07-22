from playwright.sync_api import Page, ElementHandle

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
    
    def load(self):
        self.page.goto('https://example.com/login')
    
    def set_username(self, username: str):
        self.page.fill('input[name="username"]', username)
    
    def set_password(self, password: str):
        self.page.fill('input[name="password"]', password)
    
    def click_login_button(self):
        self.page.click('button[type="submit"]')
    
    def get_error_message(self) -> str:
        error_elem: ElementHandle = self.page.query_selector('.error-message')
        if error_elem:
            return error_elem.text_content()
        return ''
