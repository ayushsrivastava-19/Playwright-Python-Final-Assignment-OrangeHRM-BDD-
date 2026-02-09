import re

from playwright.sync_api import expect
from pytest_bdd import scenarios, given, when, then, parsers

from pages.login_page import LoginPage
from pages.myInfo_page import MyInfoPage

scenarios('../features/my-info.feature')

@given(parsers.parse('the user is logged into OrangeHRM as an ESS user with username "{username}" and password "{password}"'))
def login_as_ess(page, username, password):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(username, password)

@when("the user clicks on the My Info tab")
def click_on_My_Info_tab(page):
    myInfo_page = MyInfoPage(page)
    myInfo_page.clickMy_Info()

@then("the user should be redirected to the Personal Details section")
def verify_personal_details(page):
    expect(page).to_have_url(re.compile(r".*PersonalDetails.*"))