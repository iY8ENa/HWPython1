import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class ShoppingCartTest(unittest.TestCase):
    def setUp(self):
        """Инициализируем веб-драйвер"""
        service = Service(r"C:\API UI\chromedriver.exe")
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("https://www.saucedemo.com/")

    def tearDown(self):
        """Закрываем браузер после выполнения тестов"""
        self.driver.quit()

    def test_shopping_cart_flow(self):
        """
        Тестируем процесс покупки товаров на сайте SauceDemo.
        """
        # Авторизация
        username_input = self.driver.find_element(By.ID, "user-name")
        password_input = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.ID, "login-button")

        username_input.send_keys("standard_user")
        password_input.send_keys("secret_sauce")
        login_button.click()

        # Ожидаем открытия страницы инвентаря
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("inventory.html")
        )

        # Добавляем товары в корзину
        backpack_add_button = self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-backpack")
        tshirt_add_button = self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        onesie_add_button = self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-onesie")

        backpack_add_button.click()
        tshirt_add_button.click()
        onesie_add_button.click()

        # Переходим в корзину
        shopping_cart_link = self.driver.find_element(
            By.CLASS_NAME, "shopping_cart_link")
        shopping_cart_link.click()

        # Нажимаем на кнопку Checkout
        checkout_button = self.driver.find_element(By.ID, "checkout")
        checkout_button.click()

        # Заполняем форму своими данными
        first_name_input = self.driver.find_element(By.ID, "first-name")
        last_name_input = self.driver.find_element(By.ID, "last-name")
        postal_code_input = self.driver.find_element(By.ID, "postal-code")

        first_name_input.send_keys("Андрей")
        last_name_input.send_keys("Савко")
        postal_code_input.send_keys("141108")

        # Нажимаем на кнопку Continue
        continue_button = self.driver.find_element(By.ID, "continue")
        continue_button.click()

        # Чтение итоговой стоимости
        total_cost = self.driver.find_element(
            By.CLASS_NAME, "summary_total_label").text.replace(
            "Total: ", "")
        print("Итоговая стоимость:", total_cost)

        # Проверка, что итоговая сумма равна $58.29
        self.assertEqual(
            total_cost,
            "$58.29",
            "Итоговая сумма не равна $58.29.")


if __name__ == "__main__":
    unittest.main()
