from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service

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
    driver.get("http://the-internet.herokuapp.com/inputs")

    # Нахождение поля ввода
    input_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "input")))

    # Ввод текста "1000"
    input_field.send_keys("1000")

    # Очищаем поле ввода
    input_field.clear()

    # Ввод текста "999"
    input_field.send_keys("999")

finally:
    # Закрываем браузер
    driver.quit()