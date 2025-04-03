import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestForm(unittest.TestCase):
    def setUp(self):
        """Инициализируем веб-драйвер"""
        service = Service(r"C:\API UI\chromedriver.exe")
        self.driver = webdriver.Chrome(service=service)
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        )

    def tearDown(self):
        """Закрываем браузер после выполнения тестов"""
        self.driver.quit()

    def test_form_submission(self):
        """
        Тест на заполнение и отправку формы.
        Проверяем, что поля подсвечиваются зеленым после успешной отправки,
        кроме поля Zip code, которое остается пустым и подсвечивается красным.
        """
        # Заполнение полей формы
        self.driver.find_element(By.NAME, "first-name").send_keys("Иван")
        self.driver.find_element(By.NAME, "last-name").send_keys("Петров")
        self.driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
        self.driver.find_element(
            By.NAME, "e-mail").send_keys("test@skypro.com")
        self.driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
        self.driver.find_element(By.NAME, "city").send_keys("Москва")
        self.driver.find_element(By.NAME, "country").send_keys("Россия")
        self.driver.find_element(By.NAME, "job-position").send_keys("QA")
        self.driver.find_element(By.NAME, "company").send_keys("SkyPro")

        # Оставляем поле Zip code пустым

        # Нажимаем на кнопку Submit
        self.driver.find_element(
            By.CSS_SELECTOR, ".btn.btn-outline-primary.mt-3"
        ).click()

        # Ожидаем появления сообщений об успехе/ошибке для полей
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.CLASS_NAME, "alert-success"))
        )

        # Проверяем, что поле Zip code подсвечено красным
        zip_code_error = self.driver.find_element(By.ID, "zip-code")
        self.assertIn(
            "alert-danger",
            zip_code_error.get_attribute("class"),
            "Поле Zip code не подсвечено красным!",
        )

        # Проверяем, что остальные поля подсвечены зеленым
        green_fields = [
            "first-name",
            "last-name",
            "address",
            "e-mail",
            "phone",
            "city",
            "country",
            "job-position",
            "company",
        ]
        for field_id in green_fields:
            success_message = self.driver.find_element(By.ID, field_id)
            self.assertIn(
                "alert-success",
                success_message.get_attribute("class"),
                f"Поле {field_id} не подсвечено зеленым!",
            )

    def test_invalid_zip_code(self):
        """
        Тест на отправку формы с пустым полем Zip code.
        Проверяем, что поле Zip code подсвечивается красным, а остальные поля зеленым.
        """
        # Заполнение полей формы
        self.driver.find_element(By.NAME, "first-name").send_keys("Иван")
        self.driver.find_element(By.NAME, "last-name").send_keys("Петров")
        self.driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
        self.driver.find_element(
            By.NAME, "e-mail").send_keys("test@skypro.com")
        self.driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
        self.driver.find_element(By.NAME, "city").send_keys("Москва")
        self.driver.find_element(By.NAME, "country").send_keys("Россия")
        self.driver.find_element(By.NAME, "job-position").send_keys("QA")
        self.driver.find_element(By.NAME, "company").send_keys("SkyPro")

        # Оставляем поле Zip code пустым

        # Нажимаем на кнопку Submit
        self.driver.find_element(
            By.CSS_SELECTOR, ".btn.btn-outline-primary.mt-3"
        ).click()

        # Ожидаем появления сообщений об успехе/ошибке для полей
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.CLASS_NAME, "alert-success"))
        )

        # Проверяем, что поле Zip code подсвечено красным
        zip_code_error = self.driver.find_element(By.ID, "zip-code")
        self.assertIn(
            "alert-danger",
            zip_code_error.get_attribute("class"),
            "Поле Zip code не подсвечено красным!",
        )

        # Проверяем, что остальные поля подсвечены зеленым
        green_fields = [
            "first-name",
            "last-name",
            "address",
            "e-mail",
            "phone",
            "city",
            "country",
            "job-position",
            "company",
        ]
        for field_id in green_fields:
            success_message = self.driver.find_element(By.ID, field_id)
            self.assertIn(
                "alert-success",
                success_message.get_attribute("class"),
                f"Поле {field_id} не подсвечено зеленым!",
            )


if __name__ == "__main__":
    unittest.main()
