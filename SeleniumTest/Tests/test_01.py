"""
Client
"""

import os
import sys
from dotenv import load_dotenv


from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()

path_to_add = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', '..', 'Utils'))
sys.path.append(path_to_add)


def test_01(driver):
    """
    Test 01.
    """
    driver, wait = driver

    test = wait.until(EC.element_to_be_clickable((By.ID, 'test'))).click()
    assert test.is_displayed(), "Test element is not displayed"
    assert test.text == "Test", "Test option text is not 'Test', cannot find text"
    assert test.is_enabled(), "Test element is not enabled"
    assert test.is_selected(), "Test element is not selected"
    assert test.get_attribute("placeholder") == "Test Placeholder", \
        "Test element placeholder is incorrect"
