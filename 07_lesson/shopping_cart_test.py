import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from login_page import LoginPage
from inventory_page import InventoryPage
from cart_page import CartPage
from checkout_page import CheckoutPage


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
        login_page = LoginPage(self.driver)
        login_page.enter_username("standard_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login_button()

        # Ожидаем открытия страницы инвентаря
        WebDriverWait(self.driver, 10).until(
            lambda driver: "inventory.html" in driver.current_url
        )

        # Добавляем товары в корзину
        inventory_page = InventoryPage(self.driver)
        inventory_page.add_backpack_to_cart()
        inventory_page.add_tshirt_to_cart()
        inventory_page.add_onesie_to_cart()

        # Переходим в корзину
        inventory_page.go_to_cart()

        # Нажимаем на кнопку Checkout
        cart_page = CartPage(self.driver)
        cart_page.click_checkout_button()

        # Заполняем форму своими данными
        checkout_page = CheckoutPage(self.driver)
        checkout_page.fill_first_name("Андрей")
        checkout_page.fill_last_name("Савко")
        checkout_page.fill_postal_code("141108")

        # Нажимаем на кнопку Continue
        checkout_page.click_continue_button()

        # Чтение итоговой стоимости
        total_cost = checkout_page.get_total_cost()
        print("Итоговая стоимость:", total_cost)

        # Проверка, что итоговая сумма равна $58.29
        self.assertEqual(total_cost, "$58.29", "Итоговая сумма не равна $58.29.")


if __name__ == "__main__":
    unittest.main()