from playwright.sync_api import Page,expect
import pytest
from conftest import launch_website
from locators import employee_information_locator, dropdown_locator, candidate_locator, vacancies_locator,dashboard_locator, edit_employee_locator
from locators import add_user_locator
from pages import dashboard_page
from pages import add_user
from pages import dropdown_page
from pages import candidate_page
from pages import vacancies_page
from pages import edit_employee_page
from pages import dropdown_about_page
from pages import employee_information_page

@pytest.mark.regression
def test_dashboard(launch_website):
    dashboard_page.dashboard(launch_website)
    expect(launch_website.locator(dashboard_locator.dashboard)).to_be_visible()

@pytest.mark.smoke
def test_add_user(launch_website):
    add_user.add_user(launch_website)
    expect(launch_website.locator(add_user_locator.add_user_heading)).to_be_visible()

@pytest.mark.smoke
def test_dropdown(launch_website):
    dropdown_page.dropdown_page(launch_website)
    expect(launch_website.locator(dropdown_locator.user_logout)).to_be_visible()

@pytest.mark.regression
def test_candidate(launch_website):
    candidate_page.candidate(launch_website)
    expect(launch_website.locator(candidate_locator.candidates)).to_be_visible()

@pytest.mark.regression
def test_vacancies(launch_website):
    vacancies_page.vacancies(launch_website)
    expect(launch_website.locator(vacancies_locator.vacancies)).to_be_visible()

@pytest.mark.regression
def test_edit_employee(launch_website):
    edit_employee_page.edit_employee_page(launch_website)
    expect(launch_website.locator(edit_employee_locator.add_employee)).to_be_visible()

@pytest.mark.regression
def test_dropdown_about(launch_website):
    dropdown_about_page.dropdown_about_page(launch_website)

@pytest.mark.regression
def test_employee_information(launch_website):
    employee_information_page.employee_information(launch_website)
    expect(launch_website.locator(employee_information_locator.employee_information)).to_be_visible()






















































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