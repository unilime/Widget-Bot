from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from config import CHROMEDRIVER_PATH


# Open Chrome Browser
def chrome_open(cmdopt=''):
    # Chrome driver setup
    options = Options()
    # Run headless chrome if --cmdopt 'headless'
    if cmdopt == 'headless':
        options.headless = True
        options.add_argument('window-size=1920x1080')

    return webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, options=options)


# Find element by xpath/id/class name etc.
def find_element_by(driver, path, param='xpath', click=False):
    try:
        if param == 'script':
            el = driver.execute_script(path)
        elif param == 'id':
            el = driver.find_element_by_id(path)
        elif param == 'class':
            el = driver.find_element_by_class_name(param)
        else:
            el = driver.find_element_by_xpath(path)
        if param != 'script' and click:
            try:
                el.click()
            except WebDriverException:
                return False
    except NoSuchElementException:
        return False
    return True


# Close Chrome Browser
def chrome_close(driver):
    driver.close()
    driver.quit()
