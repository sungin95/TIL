import sys
sys.stdin = open("1545.txt", "r")

a = int(input())
while a != -1:
    print(a, end=" ")
    a-= 1