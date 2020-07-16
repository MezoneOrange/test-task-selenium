from time import sleep

import pytest
from selenium.webdriver.common.keys import Keys

from pages.basepage import BasePage
from jsonparse import ParseJsonObject


MAIN_URL = 'https://yandex.ru/'


class TestChooseCity:
    """Test cases for change current city into yandex.ru site."""

    def test_open_page(self, browser):
        page = BasePage(browser, MAIN_URL)
        page.open()

    def test_existing_geo_link(self, browser):
        """The test for checking to geo link is exist."""
        page = BasePage(browser, MAIN_URL)
        page.open()
        page.should_be_geo_link()

    def test_existing_city_input_fields(self, browser):
        """The test for checking to city's input fields is exist."""
        page = BasePage(browser, MAIN_URL)
        page.open()
        page.go_to_geo_page()
        page.should_be_city_input_field()
        page.should_be_geo_checkbox()

    @pytest.mark.test
    def test_change_geo_location(self, browser):
        """Check that geo location would be changed to selected location."""
        page = BasePage(browser, MAIN_URL)
        page.open()
        page.go_to_geo_page()
        page.deactivate_geo_checkbox()

        input_field = page.get_city_input_field()
        input_field.send_keys("Moscow")
        page.push_first_geo_item()

        page.should_be_main_block()
        main = page.get_main_block()
        obj = ParseJsonObject(main.get_attribute('data-bem'))
        print(obj.get_geo_id())







