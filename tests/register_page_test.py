import time

from pages.base_page import BasePage


def test(driver):
    page = BasePage(driver, 'https://stepik.org')
    page.open()
    time.sleep(10)