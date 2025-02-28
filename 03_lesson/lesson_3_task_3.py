# lesson_3_task_3.py

from address import Address
from mailing import Mailing

# Создаем адреса
to_address = Address(index="111222", city="Москва", street="Красная", house=10, apartment=20)
from_address = Address(index="333444", city="Санкт-Петербург", street="Невский проспект", house=25, apartment=35)

# Создаем почтовое отправление
mailing = Mailing(to_address=to_address, from_address=from_address, cost=500, track="ABCD12345")

# Распечатываем информацию о почтовом отправлении
mailing.print_mailing()