import sys

sys.stdin = open("1026.txt", "r")

N = input()
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()
B.reverse()

total = 0
for i in range(int(N)):
    total += A[i] * B[i]
print(total)
