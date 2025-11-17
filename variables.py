name = "Zhakyp"
age = 20
message = f"Welcome to {name}"
my_first_name = "Zhakyp"
my_sur_name = "Zhumagulov"


y, z, x = "Orange", "Cherry", "Apple"
fruits = ["Orange", "Cherry", "Apple"]

a, b, c = fruits

q = "awesome"

def myFunc():
    global  q
    q = "fantastic"
    print(f"Python is {q}")

myFunc()

print(f"Python is {q}")

print(f"My name is {name}, I'm {age}")
print(my_sur_name, my_first_name)
print(message)
print(type(age))
print(type(name))
print(y)
print(z)
print(x)
print(a)
print(b)
print(c)