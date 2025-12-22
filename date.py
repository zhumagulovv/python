import datetime

print(datetime.datetime.now())

a = datetime.datetime.now()
b = datetime.datetime(2025, 12, 22)

print(a.year)
print(a.month)
print(a.day)

print(b)

print(a.strftime("%B"))
print(a.strftime("%Y"))
print(a.strftime("%m"))
print(a.strftime("%d"))
print(a.strftime("%y"))
print(a.strftime("%a"))
print(a.strftime("%X"))
print(a.strftime("%z"), "---")
print(a.strftime("%p"))
print(a.strftime("%j"))