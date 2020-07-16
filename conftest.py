from time import sleep

import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    yield browser
    sleep(5)
    print("\nquit browser..")
    browser.quit()
