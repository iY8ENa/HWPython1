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
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/loading-images.html')

    # Ждем загрузки конкретной картинки с id="landscape"
    landscape_img = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, 'landscape'))
    )

    # Получаем все изображения на странице
    images = driver.find_elements(By.TAG_NAME, 'img')

    # Проверяем, что изображений достаточно для получения src третьей картинки
    if len(images) >= 3:
        # Получаем src третьей картинки
        third_image_src = images[2].get_attribute('src')  # Третья картинка - images[2]
        # Выводим значение в консоль
        print(third_image_src)
    else:
        print("На странице недостаточно изображений для получения src третьей картинки.")

finally:
    # Закрываем браузер
    driver.quit()