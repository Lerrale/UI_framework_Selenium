import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os
from dotenv import load_dotenv

from locators.locators import TestShopLocators
from pages.basepage import BasePage

load_dotenv()


@pytest.fixture(scope="function")
def browser():
    """
    Инициализирует экземпляр Chrome WebDriver с заданными параметрами, открывает базовый URL,
    а после завершения теста закрывает браузер.

    Возвращает:
        WebDriver: Инициализированный драйвер для использования в тестах.
    """
    chrome_options = Options()

    # Включаем headless-режим
    chrome_options.add_argument("--headless")

    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920x1080")

    # Инициализируем браузер
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=chrome_options
    )

    # Чистим куки
    driver.delete_all_cookies()
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def test_shop_login(browser, request):
    """
    Залогинивает под пользователем standard_user
    :return:
        WebDriver: Инициализированный драйвер для использования в тестах.
    """
    login_page = BasePage(browser)
    login_page.open_url("URL_TESTSHOP")

    username = request.param

    login_page.fill_input_field(
        locator_field=TestShopLocators.LOGIN_PAGE_USERNAME_INPUT,
        data=username,
    )
    login_page.fill_input_field(
        locator_field=TestShopLocators.LOGIN_PAGE_PASSWORD_INPUT,
        data=os.getenv("PASSWORD_TESTSHOP"),
    )
    login_page.click_button(locator=TestShopLocators.LOGIN_PAGE_LOGIN_BUTTON)
    time.sleep(2)
