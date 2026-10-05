from actions import action_module
from locators import employee_information_locator
from utils import screenshot_utils


def employee_information(page):
    action_module.click(page,employee_information_locator.pim)