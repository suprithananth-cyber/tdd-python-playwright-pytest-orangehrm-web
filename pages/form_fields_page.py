from playwright.sync_api import expect

from actions import action_module
from data import form_data
from locators import form_fields_locator


def form_fields(page):
    page.goto("https://practice-automation.com/")

    action_module.click(page, form_fields_locator.form_fields_link)

    expect(page).to_have_url(
        "https://practice-automation.com/form-fields/"
    )

    page.locator(form_fields_locator.name).type(form_data.name)
    page.locator(form_fields_locator.password).type(form_data.password)

    page.locator(form_fields_locator.drink1).check()
    page.locator(form_fields_locator.drink2).check()

    page.locator(form_fields_locator.color1).check()

    page.locator(form_fields_locator.automation).select_option("yes")

    page.locator(form_fields_locator.email).type(form_data.email)
    page.locator(form_fields_locator.message).type(form_data.message)

    page.on("dialog", lambda dialog: dialog.accept())

    action_module.click(page, form_fields_locator.submit)

    expect(page).to_have_url(
        "https://practice-automation.com/form-fields/"
    )