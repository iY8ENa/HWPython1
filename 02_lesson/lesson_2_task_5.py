def month_to_season(month):
    """
    Функция принимает номер месяца и возвращает название соответствующего сезона.

    Аргументы:
    month (int): Номер месяца (от 1 до 12).

    Возвращаемые значения:
    str: Название сезона ("Зима", "Весна", "Лето", "Осень").
    """
    if month in [12, 1, 2]:
        return "Зима"
    elif month in [3, 4, 5]:
        return "Весна"
    elif month in [6, 7, 8]:
        return "Лето"
    elif month in [9, 10, 11]:
        return "Осень"
    else:
        raise ValueError("Неверный номер месяца. Должно быть от 1 до 12.")

# Пример использования функции
month_number = 2
season = month_to_season(month_number)
print(f"Месяц {month_number} относится к сезону: {season}")