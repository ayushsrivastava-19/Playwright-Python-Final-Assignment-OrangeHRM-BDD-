from playwright.sync_api import Page

class MyInfoPage(Page):
    def __init__(self, page):
        self.page = page
        self.my_info_tab = page.locator('span:has-text("My Info")')
        self.personalDetails_licenseExpiryDate = page.get_by_role("textbox", name="yyyy-dd-mm").first
        self.personalDetails_nationality = page.locator("div.oxd-select-text.oxd-select-text--active").locator("div").nth(0)
        self.personalDetails_nationalitySelect = page.get_by_role("option", name="Indian")
        self.personalDetails_saveButton = page.locator("button").filter(has_text="Save").first

    def clickMy_Info(self):
        self.my_info_tab.click()

    def select_nationality_dropdown(self):
        self.personalDetails_nationality.click()
        self.personalDetails_nationalitySelect.click()
        self.personalDetails_saveButton.click()

