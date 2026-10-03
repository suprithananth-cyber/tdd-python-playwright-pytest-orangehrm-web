from playwright.sync_api import expect
from locators import employee_information_locator
from utils import screenshot_utils
from actions import action_module

def employee_information(page):
    action_module.click(page,employee_information_locator.pim)