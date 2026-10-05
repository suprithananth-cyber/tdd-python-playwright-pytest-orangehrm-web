from actions import action_module
from locators import dashboard_locator

def dashboard(page):
    action_module.click(page,dashboard_locator.dashboard)