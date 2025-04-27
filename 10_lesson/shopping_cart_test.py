import unittest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from login_page import LoginPage
from inventory_page import InventoryPage
from cart_page import CartPage
from checkout_page import CheckoutPage
import allure

class ShoppingCartTest(unittest.TestCase):
    def setUp(self):
        """Инициализируем веб-драйвер"""
        # Указываем путь до установленного GeckoDriver
        gecko_driver_path = r"C:\API UI\geckodriver.exe"
        options = Options()
        service = Service(gecko_driver_path)
        self.driver = webdriver.Firefox(options=options, service=service)
        self.driver.get("https://www.saucedemo.com/")

    def tearDown(self):
        """Закрываем браузер после выполнения тестов"""
        self.driver.quit()

    @allure.title("Процесс покупки товаров на сайте SauceDemo")
    @allure.description("Проверка всей цепочки покупок: вход, выбор товаров, оформление заказа и просмотр итоговой стоимости.")
    @allure.feature("Покупка товаров")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_shopping_cart_flow(self):
        """
        Тестируем процесс покупки товаров на сайте SauceDemo.
        """
        # Авторизация
        with allure.step("Авторизация"):
            login_page = LoginPage(self.driver)
            login_page.enter_username("standard_user")
            login_page.enter_password("secret_sauce")
            login_page.click_login_button()

        # Ожидаем открытия страницы инвентаря
        with allure.step("Ожидаем открытия страницы инвентаря"):
            WebDriverWait(self.driver, 10).until(lambda driver: "inventory.html" in driver.current_url)

        # Добавляем товары в корзину
        with allure.step("Добавляем товары в корзину"):
            inventory_page = InventoryPage(self.driver)
            inventory_page.add_backpack_to_cart()
            inventory_page.add_tshirt_to_cart()
            inventory_page.add_onesie_to_cart()

        # Переходим в корзину
        with allure.step("Переходим в корзину"):
            inventory_page.go_to_cart()

        # Оформляем заказ
        with allure.step("Оформляем заказ"):
            cart_page = CartPage(self.driver)
            cart_page.click_checkout_button()

        # Заполняем контактные данные
        with allure.step("Заполняем контактные данные"):
            checkout_page = CheckoutPage(self.driver)
            checkout_page.fill_first_name("John")
            checkout_page.fill_last_name("Doe")
            checkout_page.fill_postal_code("12345")
            checkout_page.click_continue_button()

        # Проверяем итоговую стоимость
        with allure.step("Проверяем итоговую стоимость"):
            total_cost = checkout_page.get_total_cost()
            self.assertEqual(total_cost, "$58.29", "Итоговая сумма не равна $58.29.")

if __name__ == "__main__":
    unittest.main()