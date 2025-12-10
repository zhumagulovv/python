# Python While Loops

i = 1

while i < 6:
    print(i)
    i += 1

while i <= 6:
    print(i)
    if i == 4:
        break
    i += 1

print("----")

x = 0

while x < 6:
    x += 1
    if x == 2:
        continue
    print(i)
else:
    print("i is no longer less than 6")

print("----")

# Python For Loops
numbers = [1,2,3,4,5]
total = 0

for i in numbers:
    total += i

print(total)

print("----")

for x in "apple":
    print(x)

print("----")

for a in numbers:
    print(a)
    if a == 4:
        break
    print(a)

print("----")

for b in numbers:
    if b == 3:
        continue
    print(b)

print("----")

for c in range(5):
    print(c)

print("-----")

for d in range(2, 10, 4):
    print(d)
else:
    print("Finally finished")

print("---------")

for j in range(10):
    if j == 5: break
    print(j)

nums = [6,7,8,9,10]

for x in numbers:
    for y in nums:
        print(x, y)

for d in [1,2,3]:
    pass

print(d)