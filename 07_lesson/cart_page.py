from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")

    def click_checkout_button(self):
        checkout_button = self.driver.find_element(*self.checkout_button)
        checkout_button.click()