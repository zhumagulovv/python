def my_function():
    print("Hello everyone!")

my_function()
my_function()

def check_even_number(number):
    if number % 2 == 0:
        print(f"{number} is even number")
    else:
        print(f"{number} is odd number")


check_even_number(3)
check_even_number(10)

def fahrenheit_to_celsius(fahrenheit):
    print((fahrenheit - 32) * 2 / 6)

fahrenheit_to_celsius(20)


def say_hello(name):
    return f"Hello {name}"

print(say_hello("Asan"))

def child_names(*kids):
    print("The youngest child is " + kids[0])
    print(kids)

child_names("Amina", "Elina", "Milana")

def greeting_names(greeting, *names):
  for name in names:
    print(greeting, name)

greeting_names("Hello", "Emil", "Tobias", "Linus")

def total_points(*totals):
    sum = 0
    for i in totals:
        sum += i
    return  sum

print(total_points(2, 3,4,6,7,8,10))

def get_user(username, **user):
    print("Username", username)
    print("Email", user["email"])
    print("Password", user["password"])


get_user("Jumagulov", email="jakyp@gmail.com", password="1234qwerty")

def sum_numbers(a, b, c):
    return a + b + c

numbers = [10, 15, 20]

result = sum_numbers(*numbers)
print(result)