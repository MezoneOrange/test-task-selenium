import pytest

from pages.basepage import BasePage
from options.jsonparse import ParseMainPageObject
from options.jsonparse import ParseGeoPageObject


MAIN_URL = 'https://yandex.ru/'


class TestExistingObjects:
    """Test cases for check that some is presented, is visible, has class."""

    def test_existing_region_elements(self, browser):
        """Test case that user can see elements when starts the main page."""
        page = BasePage(browser, MAIN_URL)
        page.open()
        page.should_be_main_block()
        page.should_be_geo_link()
        page.should_be_city_name()
        page.should_be_news_region_name()
        page.should_be_maps_city_name()

    @pytest.mark.test
    def test_existing_input_fields(self, browser):
        """Test case that user can see input fields when move to the page for change geo position."""
        page = BasePage(browser, MAIN_URL)
        page.open()
        page.go_to_geo_page()
        page.should_be_city_input_field()
        page.should_be_geo_checkbox()


class TestChooseCity:
    """Test cases for change current city into yandex.ru site."""

    def test_open_page(self, browser):
        page = BasePage(browser, MAIN_URL)
        page.open()


    def test_existing_city_input_fields(self, browser):
        """The test for checking to city's input fields is exist."""
        page = BasePage(browser, MAIN_URL)
        page.open()
        page.go_to_geo_page()
        page.should_be_city_input_field()
        page.should_be_geo_checkbox()


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

        print(page.get_maps_city_name().text)
        print(page.get_news_region_name().text)
        print(page.get_city_name().text)







