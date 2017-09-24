"""
Helper functions for Selenium
"""
import os
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def create_driver():
    """
    Create driver session
    """
    capabilities = DesiredCapabilities.CHROME

    options = webdriver.ChromeOptions()
    options.add_argument('--disable-cache')
    options.add_argument('--incognito')
    options.add_argument('--ignore-certificate-errors')

    if os.getenv('DISPLAY') is not None:
        options.add_argument('--no-sandbox')

    root = os.path.dirname(os.path.dirname(__file__))
    options.add_experimental_option('prefs', {
        'download.default_directory': root,
        'safebrowsing.enabled': True,
        'profile.block_third_party_cookies': False
        })

    browser = webdriver.Chrome(desired_capabilities=capabilities, chrome_options=options)
    return browser

def wait_for_element_present(driver, by_type, value, timeout=10):
    """
    Wait for element to be present
    """
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((by_type, value))
        )
        return True
    except TimeoutException:
        return False

def wait_for_element_clickable(driver, by_type, value, timeout=10):
    """
    Wait for element to be clickable
    """
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((by_type, value))
        )
        return True
    except TimeoutException:
        return False

def hover_ui_element(driver, element):
    """
    Hover over a UI element
    """
    ActionChains(driver).move_to_element(element).perform()
