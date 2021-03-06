import requests
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .locators import BasePageLocators


class BasePage:
    """Class for communication with the main page and the geo position page.

    Contains methods for test the pages.

    """

    def __init__(self, browser, url, timeout=10):
        """Initialize webdriver.

        :param browser - selenium driver object.
        :param url - link for page.
        :param timeout - set implicitly wait time. default - 10
        """
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def click_first_geo_item(self):
        """Moves mouse to the first geo item from popup items list and click by it."""
        ActionChains(self.browser).move_to_element(self.get_first_geo_item()).click().perform()

    def deactivate_geo_checkbox(self):
        """Makes checkbox, for auto-choosing geo location, is deactivated."""
        if self.is_geo_checkbox_active():
            self.get_geo_checkbox().click()

    def get_city_input_field(self):
        """Returns input field for choosing geo location."""
        return self.browser.find_element(*BasePageLocators.GEO_INPUT_FIELD)

    def get_city_name(self):
        """Returns city name from main page."""
        return self.browser.find_element(*BasePageLocators.REGION_CITY_NAME_TITLE)

    def get_first_geo_item(self):
        """Returns the first element from item's list."""
        return self.browser.find_element(*BasePageLocators.GEO_FIRST_ITEM)

    def get_geo_checkbox(self):
        """Returns checkbox for auto-choosing geo location."""
        return self.browser.find_element(*BasePageLocators.GEO_CHECKBOX)

    def get_geo_checkbox_block(self):
        """Returns checkbox block for auto-choosing geo location."""
        return self.browser.find_element(*BasePageLocators.GEO_CHECKBOX_BLOCK)

    def get_main_block(self):
        """Returns main block in the main page."""
        return self.browser.find_element(*BasePageLocators.MAIN_JSON_BLOCK)

    def get_maps_city_name(self):
        """Returns maps city name from main page."""
        return self.browser.find_element(*BasePageLocators.REGION_CITY_NAME_TEXT)

    def get_popup_menu(self):
        """Returns popup menu from geo page."""
        return self.browser.find_element(*BasePageLocators.POPUP_MENU)

    def go_to_geo_page(self):
        """Moves to the geo position page."""
        link = self.browser.find_element(*BasePageLocators.CHOOSE_GEO_LINK)
        link.click()

    def is_element_present(self, how, what):
        """Checks element to exist by locator."""
        try:
            self.browser.find_element(how, what)
            return True
        except NoSuchElementException:
            return False

    def is_geo_checkbox_active(self):
        """Checks checkbox. If active, returns True."""
        status = 'checkbox_checked_yes'
        checkbox = self.get_geo_checkbox_block()
        return status in checkbox.get_attribute('class').split()

    def is_not_present(self, how, what, timeout=6):
        """Returns true if element is not presented."""
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_status_200(self):
        """Checks status code of request. Returns True if it = 200"""
        r = requests.get(self.url)
        return r.status_code == 200

    def should_be_city_name(self):
        """Checks that city name is presented."""
        assert self.is_element_present(*BasePageLocators.REGION_CITY_NAME_TITLE), "City name is not presented."

    def should_be_city_input_field(self):
        """Checks that city's input field is presented."""
        assert self.is_element_present(*BasePageLocators.GEO_INPUT_FIELD), "Geo city's input field is not presented."

    def should_be_first_geo_item(self):
        """Checks that first geo item is found."""
        assert self.is_element_present(*BasePageLocators.GEO_FIRST_ITEM), "First geo item is not found."

    def should_be_geo_checkbox(self):
        """Checks that geo checkbox for auto location is presented."""
        assert self.is_element_present(*BasePageLocators.GEO_CHECKBOX), "Geo checkbox is not presented."

    def should_be_geo_link(self):
        """Checks that geo link is presented in the main page."""
        assert self.is_element_present(*BasePageLocators.CHOOSE_GEO_LINK), "Geo link is not presented."

    def should_be_main_block(self):
        """Checks that main block is presented."""
        assert self.is_element_present(*BasePageLocators.MAIN_JSON_BLOCK), "Geo main block is not presented."

    def should_be_maps_city_name(self):
        """Checks that city name is presented."""
        assert self.is_element_present(*BasePageLocators.REGION_CITY_NAME_TEXT), "Geo city name is not presented."

    def should_be_popup_menu(self):
        """Checks that popup menu is presented."""
        assert self.is_element_present(*BasePageLocators.POPUP_MENU), "Popup menu is not presented."

    def should_not_be_first_geo_item(self):
        """Checks that first geo item is not found."""
        assert self.is_not_present(*BasePageLocators.GEO_FIRST_ITEM), "First geo was found."

    def open(self):
        """Open the url page."""
        if self.is_status_200():
            self.browser.get(self.url)
        else:
            assert self.is_status_200(), "Wrong status code."
