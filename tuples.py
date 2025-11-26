# index           0         1        2
this_tuples = ("Apple", "Banana", "Orange", "Cherry", "Kiwi")
(green, yellow, *blue) = this_tuples
this_number_tuples = (1,2,3,4,5,6,7,8,9,10)

print(green, "----")
print(blue)

# add tuples
c = ("Mango",)
this_tuples+= c

for i in this_tuples:
    print(i)

print(this_tuples)
# index
print(this_tuples[1])
# negative index
print(this_tuples[-1])

print(this_tuples[2:4])
print(this_tuples[:2])
print(this_tuples[3:])

if "Apple" in this_tuples:
    print(2 + 5)
else:
    print(2 - 5)

# update tuples
a = list(this_tuples)
a[1] = "Apricot"
a.append("Lemons")

a.remove("Apricot")

b = tuple(a)

print(a)
print(b)

result = this_tuples + this_number_tuples
second_result = this_number_tuples * 2

print(this_number_tuples)
print(result)
print(second_result)

# Tuple methods
f = this_number_tuples.index(7)
y = this_number_tuples.count(6)

print(f)
print(y)