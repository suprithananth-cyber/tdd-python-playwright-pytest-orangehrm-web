from playwright.sync_api import Page

from pages import form_fields_page
from pages import slider_page
from pages import calendar_page


def test_form_fields(page: Page):
    form_fields_page.form_fields(page)


def test_slider(page: Page):
    slider_page.slider(page)


def test_calendar(page: Page):
    calendar_page.calendar(page)