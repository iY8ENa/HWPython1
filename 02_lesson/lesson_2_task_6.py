# Исходный список
lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]

# Фильтруем элементы списка
filtered_elements = [item for item in lst if item < 30 and item % 3 == 0]

# Выводим результаты
print(filtered_elements)