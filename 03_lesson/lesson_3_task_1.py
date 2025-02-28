# lesson_3_task_1.py

from user import User

# Создаем нового пользователя
my_user = User(first_name="Иван", last_name="Иванов")

# Вызываем методы экземпляра my_user
my_user.print_first_name()
my_user.print_last_name()
my_user.print_full_name()
