# -*- coding: utf-8 -*-

from typing import NoReturn, Final
from xmlrpc.client import Boolean
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class BasePage(object):

    """
    Base class to initialize the base page that will be called from all pages
    """

    BASE_URL: Final = "https://www.moex.com/"
    page_uri = ""
    BASE_TITLE: Final = "Московская Биржа"
    specific_title = ""

    def __init__(self, driver: WebDriver):
        self._driver = driver
        self.wait_for_page_to_load()
        self._current_url_matches()

    # CSS locators
    _logo_image_locator = "[class=header__logo]"
    _search_input_locator = "[class*=search-field__control]"
    _change_lang_locator = "[class*=_lang]"

    # Web elements
    @property
    def logo_image(self) -> WebElement:
        return self._get_element(self._logo_image_locator)

    @property
    def search_input(self) -> WebElement:
        return self._get_element(self._search_input_locator)

    @search_input.setter
    def search_input(self, query: str) -> NoReturn:
        self.search_input.clear()
        self.search_input.send_keys(query)

    @property
    def change_lang_button(self) -> WebElement:
        return self._get_element(self._change_lang_locator)

    # Methods
    def _get_element(self, css: str) -> WebElement:
        """
        Wait for a element to be present on the screen
        :param css: css of the element to wait for
        :return: the WebElement
        """
        return self._driver.find_element_by_css_selector(css)

    def _current_url_matches(self) -> NoReturn:
        """
        Make sure the current url of the page matches the expected title
        :return:
        """
        url = self.BASE_URL + "" if self.page_uri == "" else "?{}".format(self.page_uri)
        current_url = self._driver.current_url
        assert url in current_url, "URL '{0}' not on the current URL of the page ('{1}')".format(url, current_url)

    def title_matches(self, title: str) -> Boolean:
        """
        Make sure the title of the page matches the expected title
        :return: True if the title matches the expected title
        """
        return title == self._driver.title

    def wait_for_page_to_load(self) -> NoReturn:
        """
        Wait for some web elements to show up on the screen
        :return:
        """
        self.logo_image
        self.search_input
