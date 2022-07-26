a, b = input().split()
result = ""
for chr in (a):
    result = chr + result
a = int(result)
result = ""
for chr in (b):
    result = chr + result
b = int(result)

print(a) if a > b else print(b)