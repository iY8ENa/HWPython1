from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Указываем путь до установленного ChromeDriver
chrome_driver_path = r"C:\API UI\chromedriver.exe"  #  путь

# Настройка службы ChromeDriver
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

try:
    # Шаг 1: Открыть страницу
    driver.get("http://uitestingplayground.com/dynamicid")

    # Шаг 2: Найти и кликнуть на синюю кнопку
    blue_button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
    blue_button.click()
finally:
    # Закрытие браузера после завершения работы
    driver.quit()