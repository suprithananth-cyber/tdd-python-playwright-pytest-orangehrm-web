from locators import candidate_locator
from pages import login_page


def candidate(page):
    login_page.login(page)
    page.locator(candidate_locator.topbar_tab)