import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from login_page import LoginPage
from inventory_page import InventoryPage
from cart_page import CartPage
from checkout_page import CheckoutPage
import allure


class ShoppingCartTest(unittest.TestCase):
    def setUp(self):
        """Инициализируем веб-драйвер"""
        service = Service(r"C:\API UI\chromedriver.exe")
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("https://www.saucedemo.com/")

    def tearDown(self):
        """Закрываем браузер после выполнения тестов"""
        self.driver.quit()

    @allure.title("Процесс покупки товаров на сайте SauceDemo")
    @allure.description(
        "Проверка всей цепочки покупок: вход, выбор товаров, оформление заказа и просмотр итоговой стоимости.")
    @allure.feature("Покупка товаров")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_shopping_cart_flow(self):
        """
        Тестируем процесс покупки товаров на сайте SauceDemo.
        """
        with allure.step("Авторизация"):
            login_page = LoginPage(self.driver)
            login_page.enter_username("standard_user")
            login_page.enter_password("secret_sauce")
            login_page.click_login_button()

        with allure.step("Ожидаем открытия страницы инвентаря"):
            WebDriverWait(self.driver, 10).until(lambda driver: "inventory.html" in driver.current_url)

        with allure.step("Добавляем товары в корзину"):
            inventory_page = InventoryPage(self.driver)
            inventory_page.add_backpack_to_cart()
