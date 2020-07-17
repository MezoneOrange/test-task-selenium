import pytest

from pages.basepage import BasePage
from options.jsonparse import ParseMainPageObject
from options.jsonparse import ParseGeoPageObject


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
        input_field.send_keys("Москва")
        page.should_be_first_geo_item()
        city_obj = page.get_first_geo_item()
        city = ParseGeoPageObject(city_obj.get_attribute('data-bem'))
        print(city.get_city_name(), city.get_region_name(), type(city.get_geo_id()))
        page.push_first_geo_item()

        page.should_be_main_block()
        main = page.get_main_block()
        obj = ParseMainPageObject(main.get_attribute('data-bem'))
        print(type(obj.get_geo_id()))







