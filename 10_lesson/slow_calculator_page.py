from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class SlowCalculatorPage:
    def __init__(self, driver):
        """
        Инициализирует объект страницы калькулятора.

        :param driver: Selenium WebDriver экземпляр.
        """
        self.driver = driver
        self.delay_input = (By.ID, "delay")
        self.buttons = {
            "7": (By.XPATH, "//span[@class='btn btn-outline-primary' and text()='7']"),
            "+": (By.XPATH, "//span[@class='operator btn btn-outline-success' and text()='+']"),
            "8": (By.XPATH, "//span[@class='btn btn-outline-primary' and text()='8']"),
            "=": (By.XPATH, "//span[@class='btn btn-outline-warning' and text()='=']"),
        }
        self.result_screen = (By.CLASS_NAME, "screen")

    def set_delay(self, seconds: int) -> None:
        """
        Устанавливает задержку вычислений на странице калькулятора.

        :param seconds: Количество секунд задержки.
        """
        delay_input = self.driver.find_element(*self.delay_input)
        delay_input.clear()
        delay_input.send_keys(str(seconds))

    def press_button(self, button: str) -> None:
        """
        Нажимает на определенную кнопку калькулятора.

        :param button: Текст кнопки ('7', '+', '=', etc.).
        """
        button_element = self.driver.find_element(*self.buttons[button])
        button_element.click()

    def get_result(self) -> str:
        """
        Возвращает результат вычисления с экрана калькулятора.
        Ждет, пока элемент примет значение "15".
        """
        # Ожидаем, пока элемент примет значение "15"
        WebDriverWait(self.driver, 50).until(
            EC.text_to_be_present_in_element(self.result_screen, "15")
        )
        # Получаем текст элемента
        result_div = self.driver.find_element(*self.result_screen)
        return result_div.text.strip()