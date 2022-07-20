number = 10

for i in range(1, number+1):
    a = number // i
    b = number / i
    if a == b:
        print(i, end=" ")