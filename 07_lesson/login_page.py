from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def enter_username(self, username):
        username_input = self.driver.find_element(*self.username_input)
        username_input.send_keys(username)

    def enter_password(self, password):
        password_input = self.driver.find_element(*self.password_input)
        password_input.send_keys(password)

    def click_login_button(self):
        login_button = self.driver.find_element(*self.login_button)
        login_button.click()