from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
    driver.get("http://the-internet.herokuapp.com/entry_ad")

    # Ожидаем появления модального окна
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "modal")))

    # Ожидаем появления кнопки "Close"
    close_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//p[text()='Close']")))

    # Нажимаем на кнопку "Close"
    close_button.click()

finally:
    # Закрываем браузер
    driver.quit()