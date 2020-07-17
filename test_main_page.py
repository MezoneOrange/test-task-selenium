import pytest

from pages.basepage import BasePage
from options.jsonparse import ParseMainPageObject
from options.jsonparse import ParseGeoPageObject
from options import comparison


MAIN_URL = 'https://yandex.ru/'


class TestExistingObjects:
    """Test cases for check that some is presented."""

    def test_existing_region_elements(self, browser):
        """Test case that user can see elements when starts the main page."""
        page = BasePage(browser, MAIN_URL)
        page.open()
        page.should_be_main_block()
        page.should_be_geo_link()
        page.should_be_city_name()
        page.should_be_news_region_name()
        page.should_be_maps_city_name()

    def test_existing_input_fields(self, browser):
        """Test case that user can see input fields when move to the page for change geo position."""
        page = BasePage(browser, MAIN_URL)
        page.open()
        page.go_to_geo_page()
        page.should_be_city_input_field()
        page.should_be_geo_checkbox()

    @pytest.mark.parametrize('city', ['Москва', 'Екатеринбург', 'Санкт-Петербург', 'Самара', 'Казань'])
    @pytest.mark.test
    def test_popup_item_is_found(self, browser, city):
        """Test case that user can see first item of popup menu when input correct city name.

        Test case description:

        User moves to the page for choose a geo position. Switches off checkbox. Writes in input field correct
        city name. Popup menu becomes visible. After that, he can see first item of the popup menu.

        Test programme checks that city name, that user is written, is equal to city name from json object
        that was return to the first position of popup menu.

        """
        page = BasePage(browser, MAIN_URL)
        page.open()
        page.go_to_geo_page()
        page.deactivate_geo_checkbox()

        city_input_field = page.get_city_input_field()
        city_input_field.send_keys(city)

        page.should_be_popup_menu()
        popup_menu = page.get_popup_menu()
        popup_menu_classes = popup_menu.get_attribute('class').split()
        comparison.element_within(popup_menu_classes, 'popup_visibility_visible')

        first_popup_item = page.get_first_geo_item()
        json_obj = ParseGeoPageObject(first_popup_item.get_attribute('data-bem'))
        geo_city_name = json_obj.get_city_name()
        comparison.is_equal(city, geo_city_name)


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







