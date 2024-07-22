from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self, url: str):
        self.page.goto(url)

    def fill_input(self, selector: str, text: str):
        self.page.fill(selector, text)

    def click_button(self, selector: str):
        self.page.click(selector)

    def wait_for_selector(self, selector: str):
        self.page.wait_for_selector(selector)

    def get_page_title(self) -> str:
        return self.page.title()

    def close(self):
        self.page.close()

    def get_page_content(self) -> str:
        return self.page.content()

    # Add more helper methods as needed based on your application's functionality
