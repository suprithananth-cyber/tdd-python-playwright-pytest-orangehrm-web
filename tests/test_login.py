from playwright.sync_api import Page,expect
import pytest

from locators import employee_information_locator
from pages import login_page
from pages import dashboard_page
from pages import add_user
from pages import dropdown_page
from pages import candidate_page
from pages import vacancies_page
from pages import edit_employee_page
from pages import dropdown_about_page
from pages import employee_information_page






@pytest.mark.regression
def test_dashboard(launch_website,page: Page):
    dashboard_page.dashboard(page)


def test_add_user(page: Page):
    add_user.add_user(page)


def test_dropdown(page: Page):
    dropdown_page.dropdown_page(page)


def test_candidate(page: Page):
    candidate_page.candidate(page)


def test_vacancies(page: Page):
    vacancies_page.vacancies(page)


def test_edit_employee(page: Page):
    edit_employee_page.edit_employee_page(page)


def test_dropdown_about(page: Page):
    dropdown_about_page.dropdown_about_page(page)

def test_employee_information(logged_in_page):
    employee_information_page.employee_information(logged_in_page)
    expect(logged_in_page).to_have_url(
        "https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList"
    )

    expect(
        logged_in_page.locator(employee_information_locator.employee_information)
    ).to_be_visible()






















































#<tag_name attributes>content</tag_name>
#Elements
#attribute - additional information about the content key="value"
#tag name - information about the content
#DOM - Collection of elements
#<open_tag>content<close_tag>
#locator - locating the element pages.locator('selector')
#CSS or X path - Selection - Selector
#CSS Selector - target by using tag name,attribute [key="value"], class .class_name, #id
#action