from variables import fruits

print(10 + 5)

sum = 100 + 200
sum2 = sum + 200
sum3 = sum + sum2

print(sum)
print(sum2)
print(sum3)

# Arithmetic Operators
a = 10
b = 20

# 1) Addition (+)
print(a + b)

# 2) Subtraction (-)
print(a - b)

# 3) Multiplication (*)
print(a * b)

# 4) Division (/)
print(a / b)

# 5) Modulus (%)
print(a % b)
if a % 2 == 0:
    print("Even")
else:
    print("Odd")

# 6) Exponentiation (**)
print(a ** b)

# 7) Floor division (//)
print(a // b)
print(15 % 4)

# Assignment Operators
x = 5

# 1) +=
x += 3

# 2) -=
x -= 5

# 3) *=
x *= 100

# 4) /=
x /= 3

# 5) %=
x %= 3

# 6) //=
x //= 2

print(int(x))

numbers = [1,2,3,4,5,6]
count = len(numbers)

if count > 3:
    print(f"List has {count} elements")

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")

print(count)

# Comparison Operators
# Equal ==

if a == b:
    print(a + b)
else:
    print("Not equal")

# not equal !=

if a != b:
    print(a + b)
else:
    print("Their equal")

# Greater than >

if a > b:
    print(a + b)
else:
    print(f"{a} not greater than")

# Less than <

if a < b:
    print(a + b)
else:
    print(f"{a} not less than")

# Greater than or equal to >=

for i in range(10):
    if i >= a:
        print(i)
        break;
    else:
        print(i)

# Less than or equal to <=

for i in range(10):
    if a <= i:
        print(i)
        break;
    else:
        print(i)

# Logical Operators and, or, not and

print(a > 5 and a < 20)
print(a > 5 or a < 20)
print(not(a > 5 and a < 20))

# Identity Operators (is)

g = ["banana", "cherry"]
j = ["banana", "cherry"]
n = g

print(n)

print(n is not j)
print(g == j)
print(g is j)

# Membership Operators in and in not

fruits = ["Banana", "Apple", "Cherry"]

print("Banana" in fruits)
print("apple" not in fruits)


# Bitwise Operators

# 1) AND &

print(a & b)

# 2) OR |
print(a | b)

# XOR ^
print(a ^ b)
