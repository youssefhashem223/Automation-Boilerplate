"""
Configuration for Appium tests using pytest.
This file sets up the Appium driver, handles screenshots on test failures,
"""

import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.ui import WebDriverWait

from PyUtils.Appium.login import login
from PyUtils.Appium.logout import logout

capabilities = dict(
    noReset=True,
    automationName='uiautomator2',
    language='pt',
    appPackage='com.',
    appActivity='com.',
    appWaitActivity='*',
    autoGrantPermissions=True,
)

APPIUM_SERVER_URL = 'http://localhost:4723'


@pytest.fixture(scope="function")
def start_appium_diver():
    """
    Fixture to set up the Appium driver and yield the driver and wait object.
    """
    driver = webdriver.Remote(
        APPIUM_SERVER_URL, options=UiAutomator2Options().load_capabilities(capabilities))
    wait = WebDriverWait(driver, 10)

    login(wait, driver)

    yield driver, wait

    logout(wait, driver)

    driver.quit()
