# 1️⃣ Создать tuple из 5 разных данных (строка, число, bool…)

tuple = ("apple", 12, True, 95, "Python")

print(tuple)

# 2️⃣ Вывести длину кортежа

print(len(tuple))

# 3️⃣ Вывести элементы по чётным индексам

for x in range(len(tuple)):
    if x % 2 == 0:
        print(f"{x} is even {tuple[x]}")
    # else:
    #     print(f"{x} is odd {tuple[x]}")

# 4️⃣ Проверить, есть ли элемент "Python"

if "Python" in tuple:
    print("Элемент 'Python' есть в кортеже")

# 5️⃣ Найти индекс первого появления "apple"

index = tuple.index("apple")
print(index)
print(tuple[index])