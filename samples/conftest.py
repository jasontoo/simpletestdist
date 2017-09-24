"""
Samples conftest.py
"""
import pytest
from utils import selenium_helpers

@pytest.fixture(scope="function")
def driver():
    """
    Webdriver fixture. This will start and stop a webdriver instance
    for each test.
    """
    web_driver = selenium_helpers.create_driver()
    yield web_driver
    web_driver.quit()

@pytest.fixture(scope="function", params=range(100))
def params(request):
    """
    Parametrized fixture. This will execute a test
    a fixed number of times.
    """
    return request.param
