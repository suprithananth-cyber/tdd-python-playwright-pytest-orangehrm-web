from playwright.sync_api import expect

from actions import action_module
from locators import slider_locator


def slider(page):
    page.goto("https://practice-automation.com/")
    action_module.click(page, slider_locator.slider_link)
    slider_element = page.locator(slider_locator.slider)
    slider_element.fill("50")
    expect(slider_element).to_have_value("50")