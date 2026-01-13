# Задача. Найти максимальное число в списке, не используя max().

numbers = [5, 2, 8, 1, 9]
nums = [12, 3, 45, 7, 2]

def find_max_number(numbers_arr):
    max_number = numbers_arr[0]

    for number in numbers_arr:
        if number > max_number:
            max_number = number


    return max_number




print(find_max_number(numbers), "--")
print(find_max_number(nums), "---")