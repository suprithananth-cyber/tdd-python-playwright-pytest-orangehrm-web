from actions import action_module
from locators import candidate_locator


def candidate(page):
    action_module.click(page,candidate_locator.recruitment)