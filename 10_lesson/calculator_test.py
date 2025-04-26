import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from slow_calculator_page import SlowCalculatorPage
import allure


class SlowCalculatorTest(unittest.TestCase):
    def setUp(self):
        """Инициализирует драйвер браузера и загружает страницу калькулятора."""
        service = Service(r"C:\API UI\chromedriver.exe")
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self.calculator_page = SlowCalculatorPage(self.driver)

    def tearDown(self):
        """Завершает работу драйвера после завершения тестов."""
        self.driver.quit()

    @allure.title("Тест расчета калькулятора с задержкой")
    @allure.description("Проверяет корректность вычисления суммы с временной задержкой.")
    @allure.feature("Slow Calculator")
    @allure.severity(allure.severity_level.NORMAL)
    def test_calculator_with_delay(self):
        """
        Тестирует калькулятор с фиксированной задержкой 45 секунд.

        Проверяет, что результат вычисления выражения "7 + 8" равен 15 спустя ровно 45 секунд задержки.
        """
        with allure.step("Устанавливаем задержку"):
            self.calculator_page.set_delay(45)

        with allure.step("Производим вычисления"):
            self.calculator_page.press_button("7")
            self.calculator_page.press_button("+")
            self.calculator_page.press_button("8")
            self.calculator_page.press_button("=")

        with allure.step("Получаем результат и проверяем равенство"):
            result = self.calculator_page.get_result()
            self.assertEqual(result, "15", "Результат вычисления не равен 15.")


if __name__ == "__main__":
    unittest.main()