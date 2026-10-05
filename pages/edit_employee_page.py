from actions import action_module
from locators import edit_employee_locator

def edit_employee_page(page):
    action_module.click(page, edit_employee_locator.pim)
    action_module.click(page, edit_employee_locator.add_employee)