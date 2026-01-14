# 🟢 Условия (if / else)
# Задача
#   Пользователь вводит число.
#   Если число:
#       положительное → вывести "Положительное"
#       отрицательное → "Отрицательное"
#       0 → "Ноль"

def check_number(number):
    if number == 0:
        return "Ноль"
    elif number >= 1:
        return "Положительное"
    elif number <= -1:
        return "Отрицательное"
    else:
        return number

print(check_number(1))
print(check_number(2))
print(check_number(3))

print(check_number(-4))
print(check_number(-5))

print(check_number(0))