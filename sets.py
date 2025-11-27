fruits = {"apple", "cherry", "banana"}
# fruits_second = {"Kiwi", "Apricot"}
fruits_second = ["kiwi", "apricot"]

# type
print(type(fruits))

# length
print(len(fruits))

for i in fruits:
    print(i)

print("apple" in fruits)

# add
fruits.add("orange")

fruits.update(fruits_second)

# join
fruits1 = {"mango", "plantain"}
fruits2 = {"tamarind", "passion fruit"}
fruits3 = fruits1.union(fruits2)

fruits4 = fruits1 | fruits2 | fruits3
fruits5 = fruits3 & fruits4

# remove
fruits.remove("kiwi")
fruits.discard("apricot")
fruits.pop()
# fruits.clear()

# fruits.remove("lemons") not exits lemons

print(fruits)
print(fruits3)
print(fruits4)
print(fruits5)