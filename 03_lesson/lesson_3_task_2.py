# lesson_3_task_2.py

from smartphone import Smartphone

# Создаем пустой список для каталога смартфонов
catalog = []

# Наполняем список пятью различными экземплярами класса Smartphone
catalog.append(Smartphone("Apple", "iPhone 13 Pro Max", "+79991112233"))
catalog.append(Smartphone("Samsung", "Galaxy S22 Ultra", "+79123334455"))
catalog.append(Smartphone("Xiaomi", "Mi 11 Ultra", "+79226667788"))
catalog.append(Smartphone("Huawei", "P50 Pro", "+79887776655"))
catalog.append(Smartphone("OnePlus", "9 Pro", "+79558889999"))

# Печать всего каталога в нужном формате
for phone in catalog:
    print(phone.get_info())