a = 50
b = 50

if a > b:
    print('a is greater than b')
elif a == b:
    print("a and b are equal", a + b)
else:
    print("b is greate than a")

number = 15

if number > 0:
    print('The number is positive')

is_logged_in = True

if is_logged_in:
    print("Welcome to Kyrgyzstan")

def check_even_number(check_number):
    if check_number % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")

check_even_number(20)
check_even_number(19)