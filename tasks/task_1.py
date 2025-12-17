# Вывести только чётные числа из списка

# №1
def check_even(num):
    for x in num:
        if x % 2 == 0:
            print(x)

number = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

check_even(number)

# №2
check_number = [x for x in number if x % 2 == 0]

print(check_number)