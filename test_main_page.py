import pytest

from pages.basepage import BasePage
from options.jsonparse import ParseMainPageObject
from options.jsonparse import ParseGeoPageObject
from options import comparison


MAIN_URL = 'https://yandex.ru/'


class TestChangeGeoPosition:
    """Tests for main and geo position pages of the site https://yandex.ru ."""

    @pytest.mark.is_present
    def test_existing_region_elements(self, browser):
        """Test case that user can see elements when starts the main page.

        Test case description:

        When user moves to the main page of yandex.ru he can see name of city in map link and navigation bar, also,
        can see link to the page for change his geo position.

        """
        page = BasePage(browser, MAIN_URL)
        page.open()
        page.should_be_main_block()
        page.should_be_geo_link()
        page.should_be_city_name()
        page.should_be_maps_city_name()

    @pytest.mark.is_present
    def test_existing_input_fields(self, browser):
        """Test case that user can see input fields when move to the page for change geo position.

        When user moves to the page for change geo position he can see input field for search another geo position and
        checkbox for autodetect geo position.

        """
        page = BasePage(browser, MAIN_URL)
        page.open()
        page.go_to_geo_page()
        page.should_be_city_input_field()
        page.should_be_geo_checkbox()

    @pytest.mark.parametrize('city', ['Москва', 'Екатеринбург', 'Санкт-Петербург', 'Самара', 'Казань'])
    @pytest.mark.is_present
    def test_popup_item_is_found(self, browser, city):
        """Test case for checks that user can see first item of popup menu when input correct city name.

        Test case description:

        User moves to the page for choose a geo position. Switches off checkbox. Fills input field with correct
        city name. Popup menu becomes visible. After that, he can see first item of the popup menu.

        The programme checks that city name, that user is written, is equal city name from json object
        that was returned the first position of popup menu.

        """
        page = BasePage(browser, MAIN_URL)
        page.open()
        page.go_to_geo_page()
        page.deactivate_geo_checkbox()

        city_input_field = page.get_city_input_field()
        city_input_field.clear()
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
    @pytest.mark.wrong_input
    def test_popup_item_is_not_found(self, browser, city):
        """Test case for checks that user doesn't see popup menu if input blank or incorrect city name.

        Test case description:

        User moves to the page for choose a geo position. Switches off checkbox. fills input field with incorrect
        city name or doesn't write anything. Popup menu stays invisible.

        """
        page = BasePage(browser, MAIN_URL)
        page.open()
        page.go_to_geo_page()
        page.deactivate_geo_checkbox()

        city_input_field = page.get_city_input_field()
        city_input_field.clear()
        city_input_field.send_keys(city)
        page.should_not_be_first_geo_item()

    @pytest.mark.parametrize('city', ['Москва', 'Екатеринбург', 'Санкт-Петербург', 'Самара', 'Казань'])
    @pytest.mark.choose_location
    def test_choose_geo_position(self, browser, city):
        """Test case for checks that geo position would equal to sent data.

        Test case description:

        User moves to the page for choose a geo position. Switches off checkbox. Fills input field with correct
        city name. Popup menu becomes visible.

        The programme gets geoid and city name from the json object that first item of popup menu will return.

        User clicks by the first element of popup menu and redirects to the main page with new geo position.

        The programme gets geoid from the json object that will be received in the main 'div' block in the main page.
        Also, gets city name from the navigation block and the map link block. And compares all these variables with
        those which were got from the geo position page.

        """
        page = BasePage(browser, MAIN_URL)
        page.open()
        page.go_to_geo_page()
        page.deactivate_geo_checkbox()

        city_input_field = page.get_city_input_field()
        city_input_field.clear()
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

    @pytest.mark.parametrize('city_from, city_to', [('Москва', 'Екатеринбург'),
                                                    ('Екатеринбург', 'Санкт-Петербург'),
                                                    ('Санкт-Петербург', 'Самара'),
                                                    ('Самара', 'Казань'),
                                                    ('Казань', 'Москва')])
    @pytest.mark.choose_location
    def test_data_in_main_page_will_change(self, browser, city_from, city_to):
        """Test case for checks that geo position would be changed.

        Test case description:

        User moves to the page for choose a geo position. Switches off checkbox. Fills input field with correct
        city name. Popup menu becomes visible. User clicks by the first element of popup menu and redirects
        to the main page with new geo position.

        The programme gets geoid from the json object that will be received in the main 'div' block in the main page.
        Also, gets city name from the navigation block and the map link block.

        After that, user moves to the page for choose a geo position. Fills input field with another correct city name.
        Popup menu becomes visible. User clicks by the first element of popup menu and redirects to the main page
        with new geo position.

        The programme also gets geoid, city name from the navigation block and the map link block another geo position.
        Compares they variables with previous variables there are must be different.

        """
        page = BasePage(browser, MAIN_URL)
        page.open()
        page.go_to_geo_page()
        page.deactivate_geo_checkbox()

        city_input_field_from = page.get_city_input_field()
        city_input_field_from.clear()
        city_input_field_from.send_keys(city_from)
        page.click_first_geo_item()

        main_item_from = page.get_main_block()
        main_item_from = ParseMainPageObject(main_item_from.get_attribute('data-bem'))
        from_geo_id = main_item_from.get_geo_id()
        from_title_city_name = page.get_city_name().text
        from_map_city_name = page.get_maps_city_name().text

        page.go_to_geo_page()
        city_input_field = page.get_city_input_field()
        city_input_field.clear()
        city_input_field.send_keys(city_to)
        page.click_first_geo_item()

        main_item_to = page.get_main_block()
        main_item_to = ParseMainPageObject(main_item_to.get_attribute('data-bem'))
        to_geo_id = main_item_to.get_geo_id()
        to_title_city_name = page.get_city_name().text
        to_map_city_name = page.get_maps_city_name().text

        comparison.is_not_equal(from_geo_id, to_geo_id)
        comparison.is_not_equal(from_title_city_name, to_title_city_name)
        comparison.is_not_equal(from_map_city_name, to_map_city_name)