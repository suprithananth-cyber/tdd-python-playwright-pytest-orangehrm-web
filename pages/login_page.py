from actions import action_module
from locators import login_locator


from actions import action_module
from data import login_data
from locators import login_locator


def login(page):
    page.goto(
        "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login",
    )

    page.locator(login_locator.name).type(login_data.username)
    page.locator(login_locator.password).type(login_data.password)

    action_module.click(page, login_locator.submit)
