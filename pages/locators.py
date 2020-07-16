from selenium.webdriver.common.by import By


class BasePageLocators:
    CHOOSE_GEO_LINK = (By.CSS_SELECTOR, 'a.geolink')
    GEO_INPUT_FIELD = (By.CSS_SELECTOR, '.input__box .input__input')