fruits = ["Apple", "banana", "Mango", "orange", "Kiwi"]
nums = [0, 8, 18, 35, 1,2,34,5]
new_fruits = []
a = 0

# loop
for x in fruits:
    print(x)

for i in range(len(fruits)):
    print(fruits[i], "------")

while i < len(fruits):
    print(fruits[i])
    i = i + 1

[print(b) for b in fruits]

# List Comprehension
# variant number one
for i in fruits:
    if "O" in i:
        new_fruits.append(i)

print(new_fruits)

# variant number two
new_fruit = [s for s in fruits if "K" in s]

print(new_fruit)

fruits_new = [d for d in fruits if d != "Orange"]

print(fruits_new)

numbers = [a for a in range(10) if a > 0]

print(numbers)

set_fruits = [x.upper() for x in fruits]

print(set_fruits)

# new_fruit_list = ["Apricot" for x in fruits]
#
# print(new_fruit_list)

new_list = [x if x != "Banana" else "Orange" for x in fruits]

print(new_list)

# Sort Lists

def myFunc(n):
    return abs(n - 5)

fruits.sort(reverse=True)
nums.sort(reverse=False)
nums.sort(key=myFunc)
fruits.sort(key=str.lower)
fruits.reverse()



print(fruits)
print(nums)

# copy lists
my_list = fruits.copy()
my_list_copy = list(fruits)
my_list_copy.reverse()
my_list_copy_second = fruits[:2]

print(my_list)
print(my_list_copy)
print(my_list_copy_second)

# Join lists

fruits.sort()
nums.sort()
# variant number one
third_lists = fruits + nums

# variant number two
for i in fruits:
    nums.append(i)

# variant number three
fruits.extend(nums)

print(third_lists)
print(nums)
print(fruits)