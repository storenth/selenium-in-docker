from typing import Final

import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base import BasePage


class TestBase(object):

    TESTING_URL: Final[str] = "https://www.moex.com/"

    @staticmethod
    @pytest.fixture(scope="function")
    def go_to_base_page(get_driver: WebDriver) -> BasePage:
        """Open the browser and go to the Base webpage"""
        get_driver.get(TestBase.TESTING_URL)
        return BasePage(get_driver)
