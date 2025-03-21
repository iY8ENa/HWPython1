from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Указываем путь к драйверу Chrome (ChromeDriver)
CHROME_DRIVER_PATH = r'C:\API UI\chromedriver.exe'

# Настройки для запуска Chrome
chrome_options = webdriver.ChromeOptions()
service = Service(CHROME_DRIVER_PATH)

# Инициализация драйвера Chrome
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Переходим на страницу
    driver.get('http://uitestingplayground.com/textinput')

    # Ждем появления поля ввода
    input_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'newButtonName'))
    )

    # Вводим текст "SkyPro" в поле ввода
    input_field.clear()  # Сначала очищаем поле ввода
    input_field.send_keys('SkyPro')

    # Нажимаем на синюю кнопку
    button = driver.find_element(By.ID, 'updatingButton')  # Используем ID кнопки
    button.click()

    # Получаем текст кнопки и выводим его в консоль
    new_button_text = driver.find_element(By.ID, 'updatingButton').text
    print(new_button_text)

finally:
    # Закрываем браузер
    driver.quit()