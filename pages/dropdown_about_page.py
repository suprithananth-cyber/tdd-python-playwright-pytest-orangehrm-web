from actions import action_module
from locators import dropdown_about_locator
from pages import login_page


def dropdown_about_page(page):
    login_page.login(page)

    action_module.click(page, dropdown_about_locator.user_dropdown)
    action_module.click(page, dropdown_about_locator.support)