from actions import action_module
from locators import dropdown_locator



def dropdown_page(page):
    action_module.click(page, dropdown_locator.user_dropdown)