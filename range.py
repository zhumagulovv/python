x = range(10)

print(x)

a = list(range(10))

print(a)
print(a[8])
print(a[:3])
print(a[3:])

print("-----")

b = range(0, 10, 5)

print(len(b))

print("-----")

def counter(number):
    for i in range(number):
        print(i)



counter(7)
counter(10)
counter(5)