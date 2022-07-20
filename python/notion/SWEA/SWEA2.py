a = input().split()
n = 0
for i in a:
    i = int(i)
    n += i
b = (n / 10)
print("#%d %d"% (i+1, round(b)))