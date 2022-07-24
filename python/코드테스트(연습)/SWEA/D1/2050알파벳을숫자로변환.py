import sys
sys.stdin = open("2050.txt", "r")
alpa = input()

for i in alpa:
    a= ord(i)
    a -= 64
    print(a, end=' ')