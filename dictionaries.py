car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 2025,
}

product = dict(title = "Iphone", price = 20000)

print(car)
print(type(car))

print("---")
print(product)
print(type(product))



# length
print(len(car))
print(len(product))

# get
a = car["brand"]
print(a)
print(type(a))

b = car.keys()
c = car.values()
d = car.items()
j = car.get("model")

print("----")
print(car["model"])
print(product["title"])

car["model"] = "title"



print(b)
print(c)
print(d)
print(j)

if "model" in car:
    print("Hello Model bro")
else:
    print("Bye")

# chance items
car["year"] = 2020
car.update({"year": 2023})



# Add items
car["color"] = "black"
car["body_type"] = "sedan"
car.update({"drive": "RWD"})
car["price"] = "$ 72 000"
car["mileage"] = "0, 000 km"


# remove item
# car.pop("color")
# car.popitem()
# del car["model"]
# car.clear()

print(car)

# loop for keys
for i in car:
    print(i)

# loop for keys | []
for i in car:
    print([i])

for i in car.keys():
    print(i)

# loop for values
for i in car.values():
    print(i)

# loop for items

for x,y in car.items():
    print(x,":", y)

# copy dict

my_copy_v1 = car.copy()
my_copy_v2 = dict(car)

print(my_copy_v1)
print(my_copy_v2)

cars = {
    "first": {
        "model": "Ford",
        "brand": "Mustang",
        "year": 2025
    },
    "second": {
        "model": "Audi",
        "brand": "Audi 100",
        "year": 2025
    },
    "third": {
        "model": "Toyota",
        "brand": "Camry 70",
        "year": 2025
    }
}

print(cars)
print(type(cars))

for a, obj in cars.items():
    for x in obj:
        print(x, ":", obj[x])
