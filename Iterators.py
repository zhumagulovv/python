mytuple = ("a", "b", "c")
fruit = "banana"

myiter1 = iter(mytuple)
myiter2 = iter(fruit)

print(myiter2)


print(next(myiter1))
print(next(myiter1))
print(next(myiter1))

print("-------")

print(next(myiter2))
print(next(myiter2))
print(next(myiter2))
print(next(myiter2))
print(next(myiter2))

print(type(myiter1))
print(type(mytuple))

for x in mytuple:
    print(x)

print("---------")

for x in fruit:
    print(x)

print("---------")

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
      if self.a <= 20:
          x = self.a
          self.a += 1
          return x
      else:
          raise StopIteration


myclass = MyNumbers()
myiter3 = iter(myclass)

print(next(myiter3))
print(next(myiter3))
print(next(myiter3))
print(next(myiter3))
print(next(myiter3))
print(next(myiter3))

print("---------")

for x in myiter3:
    print(x)