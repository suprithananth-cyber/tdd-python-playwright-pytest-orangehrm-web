from playwright.sync_api import expect

from data import form_data
from locators import calendar_locator


def calendar(page):
    page.goto("https://practice-automation.com/")

    page.locator(calendar_locator.calendar_link).click()

    page.locator(calendar_locator.calendar).fill(
        form_data.calendar_date
    )

    expect(page.locator(calendar_locator.date)).to_have_value(
        form_data.calendar_date
    )

    page.locator(calendar_locator.submit).click()