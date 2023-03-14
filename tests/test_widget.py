# Implementation of Selenium Test JS Widget
import pytest
from time import sleep
from config import WIDGET_URL
from includes import chrome_driver as ch
from includes import notify

test_name = 'Test JS Widget: Product - ' + WIDGET_URL


# If test failed - send message, close browser and fail test
def failed(message, driver):
    message = notify.generate_message(test_name, message)
    notify.notify_ending(message)
    ch.chrome_close(driver)
    pytest.fail(message)


def test_widget_js(cmdopt):
    # Chrome driver setup
    driver = ch.chrome_open(cmdopt)

    # Test Start: Open Widget Page
    driver.get(WIDGET_URL)
    driver.maximize_window()
    sleep(3)

    # Step1: Find wiget wrapper in page source
    step = ch.find_element_by(driver, '//div[contains(@id, "arcos_widget_wrapper")]')
    if not step:
        failed('Step1 -> Find wiget wrapper: Wrapper for widget not found!', driver)

    # Step2: Find wiget content
    step = ch.find_element_by(driver, '//div[contains(@id, "arc-widget-review")]')
    if not step:
        failed('Step2 -> Find wiget content: Content for widget not found!', driver)
    sleep(1)

    # Test end
    ch.chrome_close(driver)