import sys
sys.stdin = open("1933.txt", "r")

number = int(input())

for i in range(1, number+1):
    a = number // i
    b = number / i
    if a == b:
        print(i, end=" ")