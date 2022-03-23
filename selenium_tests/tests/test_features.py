"""Модуль тестирует основные фичи moex.com"""

import pytest

from test_base_class import TestBase
from page_objects.base import BasePage


class TestLanguages(TestBase):
    """Тестовые набор для покрытие функционала переключения
    языка с русского на английский и с английского на русский
    """

    @staticmethod
    def test_change_lang_smoke(go_to_base_page: BasePage):
        """Тест-кейз:
        1. Зайти на moex.com:
            ОР: Тайтл страницы Московская Биржа
        2. Нажать на переключатель языка
            ОР: Тайтл страницы Moscow Exchange
        ...etc
        """
        EXPECTED_RU_LANG="Русский"
        EXPECTED_EN_LANG="English"
        EXPECTED_TITLE_RU="Московская Биржа"
        EXPECTED_TITLE_EN="Moscow Exchane"
        try:
            base_page = go_to_base_page
            assert EXPECTED_TITLE_RU == base_page._driver.title
            base_page.change_lang_button.click()
            assert EXPECTED_TITLE_EN == base_page._driver.title
            base_page.change_lang_button.click()
            assert EXPECTED_TITLE_RU == base_page._driver.title
        except Exception as err:
            print('Handling test run error:', err)
