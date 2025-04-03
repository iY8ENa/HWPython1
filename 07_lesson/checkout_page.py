from selenium.webdriver.common.by import By


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.summary_total_label = (By.CLASS_NAME, "summary_total_label")

    def fill_first_name(self, firstname):
        first_name_input = self.driver.find_element(*self.first_name_input)
        first_name_input.send_keys(firstname)

    def fill_last_name(self, lastname):
        last_name_input = self.driver.find_element(*self.last_name_input)
        last_name_input.send_keys(lastname)

    def fill_postal_code(self, postalcode):
        postal_code_input = self.driver.find_element(*self.postal_code_input)
        postal_code_input.send_keys(postalcode)

    def click_continue_button(self):
        continue_button = self.driver.find_element(*self.continue_button)
        continue_button.click()

    def get_total_cost(self):
        summary_total_label = self.driver.find_element(*self.summary_total_label)
        return summary_total_label.text.replace("Total: ", "")