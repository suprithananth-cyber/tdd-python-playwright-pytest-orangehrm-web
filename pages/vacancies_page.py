from actions import action_module
from locators import vacancies_locator


def vacancies(page):
    action_module.click(page,vacancies_locator.recruitment)
    action_module.click(page,vacancies_locator.vacancies)