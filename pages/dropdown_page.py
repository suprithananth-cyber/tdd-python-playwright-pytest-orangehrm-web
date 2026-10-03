from actions import action_module
from locators import dropdown_locator
from pages import login_page


def dropdown_page(page):
    login_page.login(page)
    action_module.click(page, dropdown_locator.user_dropdown)