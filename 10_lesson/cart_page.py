from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    def __init__(self, driver):
        """
        Инициализирует объект страницы корзины.

        :param driver: Selenium WebDriver instance.
        """
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")

    def click_checkout_button(self) -> None:
        """
        Нажимает на кнопку перехода к оформлению заказа.
        """
        checkout_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.checkout_button)
        )
        checkout_button.click()