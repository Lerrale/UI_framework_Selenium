from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
import os


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_text_from_element(self, locator):
        """
        Получение текста из элемента на странице
        :param locator: Локатор для поиска элемента
        :return: Текст элемента
        """
        self.wait_for_element(locator)  # Ожидание появления элемента
        text = self.driver.find_element(*locator).text  # Извлечение текста элемента
        return text

    def fill_input_field(self, data, locator_field):
        """
        Заполнение поля ввода данными
        :param data: Информация для ввода
        :param locator_field: Локатор поля для ввода
        """
        self.wait_for_element(locator_field)  # Ожидание появления элемента
        self.driver.find_element(*locator_field).send_keys(data)  # Ввод данных в поле

    def wait_for_element(self, locator, timeout=10):
        """
        Ожидание появления элемента на странице
        :param locator: Локатор для поиска элемента
        :param timeout: Время ожидания в секундах (по умолчанию 10 секунд)
        """
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def click_button(self, locator):
        """
        Клик по кнопке на странице с использованием локатора
        :param locator: Локатор кнопки для клика
        """
        self.wait_for_element(locator)
        self.driver.find_element(*locator).click()

    def check_text_in_element(self, text_in_element, locator, strip=True):
        """
        Метод проверяет, что текст элемента соответсвует подаваемому на вход тексту.
        Метод по умолчанию удаляет пробелы в начале и конце и удаляет символ "×"
        :param text_in_element:
        :param locator:
        :param strip:
        :return: -
        """
        self.wait_for_element(locator)
        text = self.get_text_from_element(locator)
        if strip is True:
            text = text.replace("×", "").strip()
        assert text_in_element == text, f"Ошибка AR:{text}, ER:{text_in_element}"

    def open_url(self, url):
        self.driver.get(os.getenv(url))
