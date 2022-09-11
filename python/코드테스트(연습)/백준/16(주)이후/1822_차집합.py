import sys
_, __ = map(int, sys.stdin.readline().split())
A = set(map(int, sys.stdin.readline().split()))
B = set(map(int, sys.stdin.readline().split()))
answer = []
AB = (A & B)
answer = list(A ^ AB)
# for i in list(A):
#     if i not in B:
#         answer.append(i)
answer.sort()
print(len(answer))
print(*answer)
