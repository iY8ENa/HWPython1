from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        """
        Инициализирует объект страницы авторизации.

        :param driver: Selenium WebDriver instance.
        """
        self.driver = driver
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def enter_username(self, username: str) -> None:
        """
        Вводит имя пользователя в соответствующее поле.

        :param username: Имя пользователя.
        """
        username_input = self.driver.find_element(*self.username_input)
        username_input.send_keys(username)

    def enter_password(self, password: str) -> None:
        """
        Вводит пароль в соответствующее поле.

        :param password: Пароль пользователя.
        """
        password_input = self.driver.find_element(*self.password_input)
        password_input.send_keys(password)

    def click_login_button(self) -> None:
        """
        Нажимает на кнопку входа.
        """
        login_button = self.driver.find_element(*self.login_button)
        login_button.click()