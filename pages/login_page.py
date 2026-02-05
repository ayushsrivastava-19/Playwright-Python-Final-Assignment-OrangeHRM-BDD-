from playwright.sync_api import Page,expect

class LoginPage(Page):
    def __init__(self, page):
        self.page = page
        self.username_input = page.get_by_placeholder("Username")
        self.password_input = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")
        # self.error_message = page.get_by_role("p", name="Invalid credentials")
        # self.error_message = page.get_by_text("Invalid credentials")
        self.error_message = page.locator(".oxd-text.oxd-text--p.oxd-alert-content-text")

    def navigate(self):
        self.page.goto("/")

    def login(self, user, pwd):
        self.username_input.fill(user)
        self.password_input.fill(pwd)
        self.login_button.click()