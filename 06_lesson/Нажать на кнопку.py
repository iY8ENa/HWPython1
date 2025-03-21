from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Указываем путь к драйверу Chrome (ChromeDriver)
CHROME_DRIVER_PATH = r"C:\API UI\chromedriver.exe"


# Настройки для запуска Chrome
chrome_options = webdriver.ChromeOptions()
service = Service(CHROME_DRIVER_PATH)


# Инициализация драйвера Chrome
driver = webdriver.Chrome(service=service, options=chrome_options)


try:
    # Переходим на страницу
    driver.get("http://uitestingplayground.com/ajax")

    # Ждем появления кнопки (синяя кнопка)
    wait = WebDriverWait(driver, 16)
    button = wait.until(EC.element_to_be_clickable((By.ID, "ajaxButton")))  # Используем верный ID кнопки

    # Нажимаем на кнопку
    button.click()

    # Получаем текст из зеленой плашки
    green_text = wait.until(EC.visibility_of_element_located((
        By.XPATH, '//div[@id="content"]//p[@class="bg-success"]'
    ))).text

    # Выводим текст в консоль
    print(green_text)

finally:
    # Закрываем браузер
    driver.quit()