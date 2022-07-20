import sys
sys.stdin = open("2058.txt", "r")
n = input()
sum = 0
for i in n:
    sum += int(i)
print(sum)
