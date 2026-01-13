# Задача: Найти минимальное число в списке без использования min().

numbers = [6, 3, 9, 1, 5]

def find_min_numbers(numbers_array):
    min_number = numbers_array[0]

    for min_nim in numbers_array:
        if min_nim < min_number:
            min_number = min_nim


    return min_number

print(find_min_numbers(numbers))