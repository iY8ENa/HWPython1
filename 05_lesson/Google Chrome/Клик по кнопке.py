from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Указываем путь до установленного ChromeDriver
chrome_driver_path = r"C:\API UI\chromedriver.exe"

# Настройка службы ChromeDriver
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

# Шаг 1: Открыть страницу
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

# Шаг 2: Пять раз кликнуть на кнопку Add Element
add_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Add Element')]")
for _ in range(5):
    add_button.click()

# Шаг 3: Собрать со страницы список кнопок Delete
delete_buttons = driver.find_elements(By.XPATH, "//button[contains(text(), 'Delete')]")

# Шаг 4: Вывести на экран размер списка
print(f"Количество кнопок Delete: {len(delete_buttons)}")

# Закрытие браузера после завершения работы
driver.quit()