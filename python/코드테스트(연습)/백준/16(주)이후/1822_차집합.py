import sys
_, __ = map(int, sys.stdin.readline().split())
A = set(map(int, sys.stdin.readline().split()))
B = set(map(int, sys.stdin.readline().split()))
answer = []
AB = (A & B)
answer = list(A ^ AB)
answer.sort()
print(len(answer))
print(*answer)
