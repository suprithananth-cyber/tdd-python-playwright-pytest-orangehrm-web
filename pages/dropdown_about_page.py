from actions import action_module
from locators import dropdown_about_locator


def dropdown_about_page(page):
    action_module.click(page, dropdown_about_locator.user_dropdown)
    action_module.click(page, dropdown_about_locator.support)