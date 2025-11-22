# list
fruits = ["cherry", "apple", "banana", "avocado", "orange"]
tropical_fruits = ["papaya", "pineapple"]

# change lists
fruits[1] = "mango"
fruits[1:3] = ["lemons", "apricots"]
fruits[:3] = ["canary-melon", "jackfruit", "watermelon"]
fruits[3:] = ["currants", "dates-fruits", "lychees"]
fruits.insert(0, "cherimoya")

# add lists
fruits.append("kiwi")
fruits.extend(tropical_fruits)

# remove item in the lists
fruits.remove("kiwi")
fruits.pop(0)
fruits.pop()
del fruits[1]


print(fruits)
print(tropical_fruits)
print(fruits[1])
print(fruits[-2], '--')
print(len(fruits))
print(type(fruits))
print(fruits[1:3])
print(fruits[:3])
print(fruits[3:])

if "apple" in fruits:
    print("Do you want to eat apple?")
else:
    print("No, I'm not eat apple")