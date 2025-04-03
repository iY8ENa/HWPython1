import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from slow_calculator_page import SlowCalculatorPage  # Импортируем класс страницы калькулятора

class SlowCalculatorTest(unittest.TestCase):
    def setUp(self):
        """Инициализируем веб-драйвер"""
        service = Service(r"C:\API UI\chromedriver.exe")
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self.calculator_page = SlowCalculatorPage(self.driver)

    def tearDown(self):
        """Закрываем браузер после выполнения тестов"""
        self.driver.quit()

    def test_calculator_with_delay(self):
        """
        Тестируем калькулятор с заданной задержкой в 45 секунд.
        Проверяем, что результат вычисления 7 + 8 равен 15 через 45 секунд после нажатия на кнопку "=".
        """
        # Задержка 45 секунд
        self.calculator_page.set_delay(45)

        # Нажимаем на кнопки калькулятора
        self.calculator_page.press_button("7")
        self.calculator_page.press_button("+")
        self.calculator_page.press_button("8")
        self.calculator_page.press_button("=")

        # Проверяем, что результат равен 15
        result = self.calculator_page.get_result()
        self.assertEqual(result, "15", "Результат вычисления не равен 15.")

if __name__ == "__main__":
    unittest.main()