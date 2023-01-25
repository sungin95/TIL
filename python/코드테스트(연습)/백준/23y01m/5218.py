import sys

sys.stdin = open("5218.txt", "r")

T = int(input())
for t in range(T):
    alpa = input().split()
    al_1, al_2 = ([], [])
    print(alpa, al_1, al_2)
