import requests
from selenium import webdriver


class BasePage:
    """Class for communication with main page and page's for choose city.

    Initialize Chrome webdriver.

    Contains all methods for choose current city.

    """

    def __init__(self, browser, url, timeout=10):
        """Initialize Chrome webdriver.

        :param url - link for page.
        :param timeout - set implicitly wait time. default - 10
        """
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        """Open the url page."""
        if self.is_status_200():
            self.browser.get(self.url)
        else:
            assert self.is_status_200(), "Wrong status code."

    def is_status_200(self):
        """Checks status code of request. Returns True if it = 200"""
        r = requests.get(self.url)
        return r.status_code == 200
