from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime

class SlowCalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_input = (By.ID, "delay")
        self.buttons = {
            "7": (By.XPATH, "//span[@class='btn btn-outline-primary' and text()='7']"),
            "+": (By.XPATH, "//span[@class='operator btn btn-outline-success' and text()='+']"),
            "8": (By.XPATH, "//span[@class='btn btn-outline-primary' and text()='8']"),
            "=": (By.XPATH, "//span[@class='btn btn-outline-warning' and text()='=']"),
        }
        self.result_screen = (By.CLASS_NAME, "screen")

    def set_delay(self, seconds):
        delay_input = self.driver.find_element(*self.delay_input)
        delay_input.clear()
        delay_input.send_keys(str(seconds))

    def press_button(self, button):
        button_element = self.driver.find_element(*self.buttons[button])
        button_element.click()

    def get_result(self):
        # Отсчитываем 45 секунд
        target_time = datetime.datetime.now() + datetime.timedelta(seconds=45)

        # Ожидаем появления результата
        result_div = WebDriverWait(self.driver, 45).until(
            lambda driver: driver.find_element(By.CLASS_NAME, "screen") if datetime.datetime.now() >= target_time else False
        )

        # Проверяем, что результат равен 15
        return result_div.text