from selenium.webdriver.common.by import By


class CheckoutPage:
    def __init__(self, driver):
        """
        Инициализирует объект страницы оформления заказа.

        :param driver: Selenium WebDriver instance.
        """
        self.driver = driver
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.summary_total_label = (By.CLASS_NAME, "summary_total_label")

    def fill_first_name(self, firstname: str) -> None:
        """
        Заполняет поле ввода имени.

        :param firstname: Имя пользователя.
        """
        first_name_input = self.driver.find_element(*self.first_name_input)
        first_name_input.send_keys(firstname)

    def fill_last_name(self, lastname: str) -> None:
        """
        Заполняет поле ввода фамилии.

        :param lastname: Фамилия пользователя.
        """
        last_name_input = self.driver.find_element(*self.last_name_input)
        last_name_input.send_keys(lastname)

    def fill_postal_code(self, postalcode: str) -> None:
        """
        Заполняет поле ввода почтового индекса.

        :param postalcode: Почтовый индекс.
        """
        postal_code_input = self.driver.find_element(*self.postal_code_input)
        postal_code_input.send_keys(postalcode)

    def click_continue_button(self) -> None:
        """
        Нажимает на кнопку продолжения.
        """
        continue_button = self.driver.find_element(*self.continue_button)
        continue_button.click()

    def get_total_cost(self) -> str:
        """
        Возвращает итоговую стоимость заказа.

        :return: Стоимость заказа в виде строки.
        """
        summary_total_label = self.driver.find_element(*self.summary_total_label)
        return summary_total_label.text.split(":")[1].strip()