from playwright.sync_api import expect
from pages import login_page
from locators import dashboard_locator


def dashboard(page):
    login_page.login(page)
    expect(page.locator(dashboard_locator.dashboard)).to_have_text("Dashboard")