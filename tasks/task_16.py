# 🟢 Функции

# Задача. Создай функцию sum_numbers(a, b), которая возвращает сумму двух чисел.

def sum_numbers(a, b):
    return a + b

print(sum_numbers(1, 2))
print(sum_numbers(10, 20))

# Задача. Создай функцию, которая принимает список чисел и возвращает количество чётных чисел.

def even_numbers(array):
    new_even_numbers = []
    for number in array:
        if number % 2 == 0:
            new_even_numbers.append(number)

    return new_even_numbers


print(even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(even_numbers([11, 22, 33, 44, 51, 16, 17, 18, 19, 190]))