import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime


class SlowCalculatorTest(unittest.TestCase):
    def setUp(self):
        """Инициализируем веб-драйвер"""
        service = Service(r"C:\API UI\chromedriver.exe")
        self.driver = webdriver.Chrome(service=service)
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def tearDown(self):
        """Закрываем браузер после выполнения тестов"""
        self.driver.quit()

    def test_calculator_with_delay(self):
        """
        Тестируем калькулятор с заданной задержкой в 45 секунд.
        Проверяем, что результат вычисления 7 + 8 равен 15 через 45 секунд после нажатия на кнопку "=".
        """
        # Задержка 45 секунд
        delay_input = self.driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys("45")

        # Нажимаем на кнопки калькулятора
        self.driver.find_element(
            By.XPATH, "//span[@class='btn btn-outline-primary' and text()='7']").click()
        self.driver.find_element(
            By.XPATH,
            "//span[@class='operator btn btn-outline-success' and text()='+']").click()
        self.driver.find_element(
            By.XPATH, "//span[@class='btn btn-outline-primary' and text()='8']").click()
        self.driver.find_element(
            By.XPATH, "//span[@class='btn btn-outline-warning' and text()='=']").click()

        # Отсчитываем 45 секунд
        target_time = datetime.datetime.now() + datetime.timedelta(seconds=45)

        # Ожидаем появления результата
        result_div = WebDriverWait(self.driver, 45).until(
            lambda driver: driver.find_element(By.CLASS_NAME,
                                               "screen") if datetime.datetime.now() >= target_time else False
        )

        # Проверяем, что результат равен 15
        self.assertEqual(
            result_div.text,
            "15",
            "Результат вычисления не равен 15.")


if __name__ == "__main__":
    unittest.main()
