# 1️⃣ Списки (Lists)
# У тебя есть список фруктов:
# fruits = ["apple", "banana", "cherry", "banana", "mango"]
# Задание:
# Удалить один элемент "banana"
# Добавить "orange" в конец списка
# Поменять "cherry" на "grape"
# Вывести итоговый список
from functools import reduce

fruits = ["apple", "banana", "cherry", "banana", "mango"]

fruits.remove("banana")
fruits.append("orange")
fruits[2] = "grape"

print(fruits)


# 2️⃣ Кортежи (Tuples)
# У тебя есть кортеж:
# dimensions = (1920, 1080, 75)
# Задание:
# Вывести первую и последнюю величину
# Преобразовать кортеж в список, изменить частоту (последний элемент) на 144, затем снова преобразовать в кортеж

dimensions = (1920, 1080, 75)
(first, second, last) = dimensions
a = list(dimensions)
a[-1] = 144
b = tuple(a)

print(first)
print(last)
print(b)

# 3️⃣ Множества (Sets)
# Даны два множества:
# set1 = {"cat", "dog", "parrot"}
# set2 = {"dog", "lion", "tiger"}
# Задание:
# Найти общие элементы
# Объединить множества
# Добавить в set1 элемент "hamster"

set1 = {"cat", "dog", "parrot"}
set2 = {"dog", "lion", "tiger"}

common_elements_method = set1.intersection(set2)
set1.update(set2)
set1.add("hamster")

print(common_elements_method)
print(set1)

# 4️⃣ Словари (Dictionaries)
# Дан словарь студента:
# student = {
#     "name": "John",
#     "age": 18,
#     "grades": [85, 90, 78]
# }
# Задание:
# Изменить возраст на 19
# Добавить новую оценку 92
# Вывести среднюю оценку студента (через sum() и len())

student = {
    "name": "John",
    "age": 18,
    "grades": [85, 90, 78]
}

student.update({"age": 19})
student["grades"].append(92)
average = sum(student["grades"]) / len(student["grades"])

print(average)
print(student)

# Создать список из 10 чисел и вывести сумму всех элементов

numbers = [1,2,3,4,5,6,7,8,9,10]

# variant №1
print(sum(numbers))

# variant №2
sum = 0

for x in numbers:
    sum += x

print(sum)

# variant №3
total = reduce(lambda a, b: a + b, numbers)

print(total)