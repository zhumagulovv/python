# Задача: Подсчёт чётных чисел

numbers = [6, 3, 9, 1, 5, 8]
even_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)


print(even_numbers)
print(len(even_numbers))