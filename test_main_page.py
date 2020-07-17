import pytest

from pages.basepage import BasePage
from options.jsonparse import ParseMainPageObject
from options.jsonparse import ParseGeoPageObject
from options import comparison


MAIN_URL = 'https://yandex.ru/'


class TestChangeGeoPosition:
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
    def test_popup_item_is_found(self, browser, city):
        """Test case for checks that user can see first item of popup menu when input correct city name.

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

    @pytest.mark.parametrize('city', ['', ' ', 'териненг', 'врвапаывап', 'Cаmаpа', 'Казнь ыыв'])
    def test_popup_item_is_not_found(self, browser, city):
        """Test case for checks that user doesn't see popup menu if input blank or incorrect city name.

        Test case description:

        User moves to the page for choose a geo position. Switches off checkbox. Writes in input field incorrect
        city name or doesn't write anything. Popup menu stays invisible.

        """
        page = BasePage(browser, MAIN_URL)
        page.open()
        page.go_to_geo_page()
        page.deactivate_geo_checkbox()

        city_input_field = page.get_city_input_field()
        city_input_field.send_keys(city)
        page.should_not_be_first_geo_item()

    @pytest.mark.parametrize('city', ['Москва', 'Екатеринбург', 'Санкт-Петербург', 'Самара', 'Казань'])
    @pytest.mark.test
    def test_change_geo_position(self, browser, city):
        """Test case for checks that geo position would be changed.

        Test case description:

        User moves to the page for choose a geo position. Switches off checkbox. Writes in input field correct
        city name. Popup menu becomes visible.

        Programme gets geoid and city name from the json object that first item of popup menu will return.

        User clicks by the first element of popup menu and redirects the to main page with new geo position.

        Programme gets geoid from the json object that will be received in the main 'div' block in the main page.
        Also, gets city name from navigation block and map link block. And compares all these variables with those
        which were got from the geo position page.

        """
        page = BasePage(browser, MAIN_URL)
        page.open()
        page.go_to_geo_page()
        page.deactivate_geo_checkbox()

        city_input_field = page.get_city_input_field()
        city_input_field.send_keys(city)

        popup_item = page.get_first_geo_item()
        popup_item = ParseGeoPageObject(popup_item.get_attribute('data-bem'))
        popup_geo_id = popup_item.get_geo_id()
        popup_city_name = popup_item.get_city_name()
        page.click_first_geo_item()

        main_item = page.get_main_block()
        main_item = ParseMainPageObject(main_item.get_attribute('data-bem'))
        main_geo_id = main_item.get_geo_id()
        title_city_name = page.get_city_name().text
        map_city_name = page.get_maps_city_name().text

        comparison.is_equal(popup_geo_id, main_geo_id)
        comparison.is_equal(popup_city_name, title_city_name)
        comparison.element_within(map_city_name, popup_city_name[:-1])

