import sys

sys.stdin = open("2011.txt", "r")

code = input()

n = len(code)
a = n // 2
b = n % 2

check_dict = {}
check = []
for i in range(1, 27):
    check_dict[str(i)] = "check"
for i in range(1, len(code)):
    num = code[i - 1] + code[i]
    if check_dict.get(num) == None:
        check.append(i)

minus = 0
if b == 0:
    for c in check:
        if c % 2 == 0:
            minus += a - 1
        else:
            minus += a
else:
    for c in check:
        minus += a

fibo = [1, 1]

for i in range(1, n):
    new = fibo[i - 1] + fibo[i]
    fibo.append(new)

print((fibo[-1] - minus) % 1000000)
