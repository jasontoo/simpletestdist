"""
Sample test case with Selenium
"""
import math
from time import sleep
from selenium.webdriver.common.by import By
from utils import selenium_helpers


def test_sample(driver):
    """
    test_sample
    """
    driver.get('https://www.google.com')
    assert selenium_helpers.wait_for_element_present(driver, By.ID, 'lst-ib')

def test_multiple(driver, params):
    """
    test_multiple
    """
    driver.get('https://www.google.com')
    assert selenium_helpers.wait_for_element_present(driver, By.ID, 'lst-ib')

def test_performance(params):
    """
    test_performance
    """
    math.factorial(params)
    sleep(1)
    assert True
