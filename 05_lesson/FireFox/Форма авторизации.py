from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service  # Добавляем импорт Service

# Указываем путь до установленного GeckoDriver
gecko_driver_path = r"C:\API UI\geckodriver.exe"  #  путь

# Настройка службы GeckoDriver
service = Service(executable_path=gecko_driver_path)

# Настройка опций Firefox
options = webdriver.FirefoxOptions()
options.headless = False

# Инициализация драйвера Firefox
driver = webdriver.Firefox(service=service, options=options)

try:
    # Открываем страницу
    driver.get("http://the-internet.herokuapp.com/login")

    # Нахождение полей ввода и кнопки Login
    username_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password")))
    login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.TAG_NAME, "button")))

    # Вводим данные в поля
    username_input.send_keys("tomsmith")
    password_input.send_keys("SuperSecretPassword!")

    # Нажимаем кнопку Login
    login_button.click()

finally:
    # Закрываем браузер
    driver.quit()