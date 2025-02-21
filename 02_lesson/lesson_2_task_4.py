def fizz_buzz(n):
    """
    Функция печатает числа от 1 до n, заменяя некоторые числа на Fizz, Buzz или FizzBuzz.

    Аргументы:
    n (int): Верхняя граница диапазона чисел.
    """
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# Пример использования функции
n = 20  # Задаем верхнюю границу
fizz_buzz(n)