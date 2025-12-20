import say_name
import sum_two_number as sum
import calculate
import platform


from calculate import add

say_name.say_name("Zhakyp")

print(sum.sum_two_number(10, 20))
print(sum.sum_two_number(30, 20))

print(calculate.add(20, 40))
print(calculate.subtract(20, 40))
print(calculate.multiply(20, 40))
print(calculate.divide(20, 40))

a = platform.system()
print(a)

b = dir(platform)
print(b)

print(add(30, 30))