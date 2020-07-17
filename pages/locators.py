from selenium.webdriver.common.by import By


class BasePageLocators:
    CHOOSE_GEO_LINK = (By.CSS_SELECTOR, 'a.geolink')
    GEO_INPUT_FIELD = (By.CSS_SELECTOR, '.input__box .input__input')
    GEO_CHECKBOX = (By.CSS_SELECTOR, 'input.checkbox__control')
    GEO_CHECKBOX_BLOCK = (By.CSS_SELECTOR, 'span.checkbox')
    GEO_FIRST_ITEM = (By.CSS_SELECTOR, 'div.popup__content > ul > li:nth-child(1)')
    MAIN_JSON_BLOCK = (By.CSS_SELECTOR, 'div.rows__row_main > div.main')
    REGION_CITY_NAME_TEXT = (By.CSS_SELECTOR, '.region__cityname_text')
    REGION_CITY_NAME_TITLE = (By.CSS_SELECTOR, 'a.home-link.geolink > span.geolink__reg')
    POPUP_MENU = (By.CSS_SELECTOR, 'div.popup')
