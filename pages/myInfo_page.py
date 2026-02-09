from playwright.sync_api import Page

class MyInfoPage(Page):
    def __init__(self, page):
        self.page = page
        self.my_info_tab = page.locator('span:has-text("My Info")')

    def clickMy_Info(self):
        self.my_info_tab.click()


