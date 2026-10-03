from playwright.sync_api import expect

from actions import action_module
from locators import add_user_locator
from pages import login_page


def add_user(page):
    login_page.login(page)

    action_module.click(page, add_user_locator.admin)
    action_module.click(page, add_user_locator.add_user)

    expect(page).to_have_url(
        "https://opensource-demo.orangehrmlive.com/web/index.php/admin/saveSystemUser"
    )