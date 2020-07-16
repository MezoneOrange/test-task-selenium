import pytest

from conftest import browser
from pages.basepage import BasePage


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

    @pytest.mark.test
    def test_existing_city_input_field(self, browser):
        """The test for checking to city's input field is exist."""
        page = BasePage(browser, MAIN_URL)
        page.open()
        page.go_to_geo_page()
        page.should_be_city_input_field()
        page.should_be_geo_checkbox()





