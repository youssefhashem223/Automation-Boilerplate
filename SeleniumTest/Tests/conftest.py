"""
Configuration file for pytest to set up the Selenium WebDriver and login/logout functionality.
"""
import os
import pytest
from dotenv import load_dotenv


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from SeleniumTest.Utils.logout import logout
from SeleniumTest.Utils.login import login

load_dotenv()


@pytest.fixture(scope="function")
def start_driver():
    """
    Fixture to set up the Selenium WebDriver, log in to the application, 
    and yield the driver and wait object.
    """
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 5)

    driver.get(os.getenv("URL"))

    login(wait, driver)

    yield driver, wait

    logout(wait, driver)

    driver.quit()
