from selenium import webdriver


class BasePage:
    """Class for communication with main page and page's for choose city.

    Initialize Chrome webdriver.

    Contain all methods for choose current city.

    """

    def __init__(self, url, timeout=10):
        """Initialize Chrome webdriver.

        :param url - link for page.
        :param timeout - set implicitly wait time. default - 10
        """
        self.browser = webdriver.Chrome()
        self.url = url
        self.browser.implicitly_wait(timeout)