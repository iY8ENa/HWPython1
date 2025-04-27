from selenium.webdriver.common.by import By


class InventoryPage:
    def __init__(self, driver):
        """
        Инициализирует объект страницы товарного инвентаря.

        :param driver: Selenium WebDriver instance.
        """
        self.driver = driver
        self.backpack_add_button = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.tshirt_add_button = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        self.onesie_add_button = (By.ID, "add-to-cart-sauce-labs-onesie")
        self.shopping_cart_link = (By.CLASS_NAME, "shopping_cart_link")

    def add_backpack_to_cart(self) -> None:
        """
        Добавляет рюкзак в корзину.
        """
        backpack_add_button = self.driver.find_element(*self.backpack_add_button)
        backpack_add_button.click()

    def add_tshirt_to_cart(self) -> None:
        """
        Добавляет футболку в корзину.
        """
        tshirt_add_button = self.driver.find_element(*self.tshirt_add_button)
        tshirt_add_button.click()

    def add_onesie_to_cart(self) -> None:
        """
        Добавляет комбинезон в корзину.
        """
        onesie_add_button = self.driver.find_element(*self.onesie_add_button)
        onesie_add_button.click()

    def go_to_cart(self) -> None:
        """
        Переход в корзину покупок.
        """
        shopping_cart_link = self.driver.find_element(*self.shopping_cart_link)
        shopping_cart_link.click()