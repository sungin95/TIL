import sys

sys.stdin = open("11725.txt", "r")

N = int(input())
tree = [[] for i in range(N + 1)]
answer_dict = {}
for _ in range(N - 1):
    v1, v2 = map(int, input().split())
    tree[v1].append(v2)
    tree[v2].append(v1)

start = 1
visited = [False] * (N + 1)
visited[1] = True

stack = [1]
while stack:
    cur = stack.pop()
    for t in tree[cur]:
        if visited[t] == False:
            visited[t] = True
            stack.append(t)
            answer_dict[t] = cur

for i in range(2, N + 1):
    print(answer_dict[i])
