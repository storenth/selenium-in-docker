import pytest

from test_base_class import TestBase
from page_objects.base import BasePage


class TestSearches(TestBase):

    @staticmethod
    # @pytest.mark.parametrize("fake_search", ["ishdbidsfba", "iehbfisbfibwf", "pewnfeowhfo"])
    def test_ru_lang_smoke(go_to_base_page: BasePage):
        """
        Search for a non existing product
        :param go_to_base_page: fixture to open the browser and go to the base page
        :return:
        """
        base_page = go_to_base_page
        base_page._driver.get_screenshot_as_file("/selenium_tests/screenshots/moex.png")
        # search_page = base_page.search_product(fake_search)
        # error_msg = "Some results are found even after using the random string '{}'".format(fake_search)
        assert "Московская Бирба" == base_page._driver.title
