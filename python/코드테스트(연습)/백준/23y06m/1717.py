import sys

sys.stdin = open("1717.txt", "r")
sys.setrecursionlimit(1000000)  # 재귀 깊이 제한 늘리기

N, M = map(int, input().split())

answer = []


def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


parent = [i for i in range(N + 1)]

for i in range(M):
    order, a, b = map(int, input().split())
    if order == 0:
        a = find_parent(a)
        b = find_parent(b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    elif order == 1:
        if find_parent(a) == find_parent(b):
            answer.append("YES")
        else:
            answer.append("NO")
for ans in answer:
    print(ans)
# print(parent)
# for i in range(1, N + 1):
#     a = find_parent(i)
#     print(a)

# print(parent)
