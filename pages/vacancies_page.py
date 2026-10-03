from locators import vacancies_locator
from pages import login_page

def vacancies(page):
    login_page.login(page)
    page.locator(vacancies_locator.topbar_tab)