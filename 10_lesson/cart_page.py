from selenium.webdriver.common.by import By


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
        Нажимает на кнопку перехода к оплате.
        """
        checkout_button = self.driver.find_element(*self.checkout_button)
        checkout_button.click()