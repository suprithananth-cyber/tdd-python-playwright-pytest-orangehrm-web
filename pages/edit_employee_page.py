from actions import action_module
from locators import edit_employee_locator
from pages import login_page

def edit_employee_page(page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/pim/contactDetails/empNumber/7")
    login_page.login(page)
    action_module.click(page, edit_employee_locator.edit_employee)