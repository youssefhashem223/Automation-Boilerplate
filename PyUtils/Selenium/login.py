"""
Login utility for Selenium tests.
"""

import os
import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from dotenv import load_dotenv
load_dotenv()

path_to_add = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
sys.path.append(path_to_add)


def login(wait, _driver):
    """"
    Login from the application.
    """

    enter = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//a[@href='/login']")))
