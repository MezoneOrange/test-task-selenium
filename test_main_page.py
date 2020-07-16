from time import sleep

import pytest

from conftest import browser
from pages.basepage import BasePage


MAIN_URL = 'https://yandex.ru/'


class TestChooseCity:
    """Test cases for change current city into yandex.ru site."""

    def test_open_page(self, browser):
        page = BasePage(browser, MAIN_URL)
        page.open()
        sleep(10)

    def test_existing_geo_link(self, browser):
        """The test for checking to geo link is exist."""
        page = BasePage(browser, MAIN_URL)
        page.open()
        page.should_be_geo_link()
        sleep(5)

    @pytest.mark.test
    def test_existing_city_input_field(self, browser):
        """The test for checking to city's input field is exist."""
        page = BasePage(browser, MAIN_URL)
        page.open()
        page.go_to_geo_page()


if __name__ == '__main__':
    page = TestChooseCity()
    page.test_open_page()
    sleep(10)
