from actions import action_module
from locators import add_user_locator


def add_user(page):
    action_module.click(page, add_user_locator.admin)
    action_module.click(page, add_user_locator.add_user)