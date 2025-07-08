"""
Login utility for Selenium tests.
"""

import os
import sys
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy

from dotenv import load_dotenv
load_dotenv()

path_to_add = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
sys.path.append(path_to_add)


def logout(wait, driver):
    """"
    Logout from the application.
    """

    exit = wait.until(EC.element_to_be_clickable(
        (AppiumBy.ID, 'exit')))
