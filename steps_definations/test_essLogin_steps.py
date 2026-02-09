import re

from pytest_bdd import scenarios, given, when, then, parsers
from pages.login_page import LoginPage
from playwright.sync_api import expect
from utils.data_reader import get_data

scenarios('../features/ESSlogin.feature')

@given('the user launches the OrangeHRM portal')
def open_url(page):
    login_page = LoginPage(page)
    login_page.navigate()

# @when(parsers.parse('the user enters credentials for "{user_type}"')) //using users.json
# def enter_creds(page, user_type):
#     credentials = get_data(user_type)
#     login_page = LoginPage(page)
#     login_page.login(credentials['username'], credentials['password'])

@when(parsers.parse('the user enters username "{username}" and password "{password}"'))
def enter_creds(page, username, password):
    login_page = LoginPage(page)
    login_page.login(username, password)

@when('clicks on the login button')
def click_login(page):
    pass

@then('the user should be redirected to the dashboard page')
def verify_login(page):
    expect(page).to_have_url(re.compile(r".*dashboard.*"))