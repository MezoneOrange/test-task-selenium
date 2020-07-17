import requests
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from .locators import BasePageLocators


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

    def go_to_geo_page(self):
        """Moves to page for change geo position."""
        link = self.browser.find_element(*BasePageLocators.CHOOSE_GEO_LINK)
        link.click()

    def deactivate_geo_checkbox(self):
        """Makes checkbox for auto-choosing geo location is deactivated."""
        if self.is_geo_checkbox_active():
            self.get_geo_checkbox().click()

    def get_city_input_field(self):
        """Returns input field for choosing geo location."""
        return self.browser.find_element(*BasePageLocators.GEO_INPUT_FIELD)

    def get_geo_checkbox(self):
        """Returns checkbox for auto-choosing geo location."""
        return self.browser.find_element(*BasePageLocators.GEO_CHECKBOX)

    def get_geo_checkbox_block(self):
        """Returns checkbox block for auto-choosing geo location."""
        return self.browser.find_element(*BasePageLocators.GEO_CHECKBOX_BLOCK)

    def get_first_geo_item(self):
        """Returns first element from item's list."""
        return self.browser.find_element(*BasePageLocators.GEO_FIRST_ITEM)

    def get_main_block(self):
        """Returns main block in the main page."""
        return self.browser.find_element(*BasePageLocators.MAIN_JSON_BLOCK)

    def get_maps_city_name(self):
        """Returns main block in the main page."""
        return self.browser.find_element(*BasePageLocators.REGION_CITY_NAME_TEXT)

    def should_be_geo_link(self):
        """Checks that geo link is presented."""
        assert self.is_element_present(*BasePageLocators.CHOOSE_GEO_LINK), "Geo link is not presented."

    def should_be_geo_checkbox(self):
        """Checks that geo checkbox for auto location is presented."""
        assert self.is_element_present(*BasePageLocators.GEO_CHECKBOX), "Geo checkbox is not presented."

    def should_be_first_geo_item(self):
        """Checks that first geo item is found."""
        assert self.is_element_present(*BasePageLocators.GEO_FIRST_ITEM), "First geo item is not found."

    def should_be_city_input_field(self):
        """Checks that city's input field is presented."""
        assert self.is_element_present(*BasePageLocators.GEO_INPUT_FIELD), "Geo city's input field is not presented."

    def should_be_main_block(self):
        """Checks that main block is presented."""
        assert self.is_element_present(*BasePageLocators.MAIN_JSON_BLOCK), "Geo main block is not presented."

    def should_be_maps_city_name(self):
        """Checks that city name is presented."""
        assert self.is_element_present(*BasePageLocators.REGION_CITY_NAME_TEXT), "Geo city name is not presented."

    def is_element_present(self, how, what):
        """Checks element to exist by locator."""
        try:
            self.browser.find_element(how, what)
            return True
        except NoSuchElementException:
            return False

    def is_geo_checkbox_active(self):
        """Check checkbox. If active, returns True."""
        status = 'checkbox_checked_yes'
        checkbox = self.get_geo_checkbox_block()
        return status in checkbox.get_attribute('class').split()

    def push_first_geo_item(self):
        """Moves mouse to first geo item from found item's list and click by it."""
        ActionChains(self.browser).move_to_element(self.get_first_geo_item()).click().perform()

