# 바이러스 푸는법
# 세팅
# 접점과 접선을 받는다.
# 접점에게 각각 접점+1 만큼의 빈칸을 부여한다.(graph로 명명)
# graph는 이러한 구조를 가진다.
# [
#   [],
#   [2, 5],
#   [1, 3, 5],
#   [2],
#   [7],
#   [1, 2, 6],
#   [5],
#   [4]
# ]
# 각 접점을 방문했는지 체크판을 만든다.(visid로 명명)
# 이제 접선을 받아서 관계도를 완성해 준다.
#
# 해결
# 시작점을 정해주고, stack을 만들어 시작값을 넣어준다.
# 시작점은 방문처리를 한다.
# stack에서 시작점을 빼 주고 연결된 곳을 다시 넣고
# 넣은 곳은 방문 처리 해 준다.
#
from pprint import pprint
import sys

sys.stdin = open("2606.txt", "r")

N = int(input())
M = int(input())

graph = []
visited = []

for i in range(N + 1):
    graph.append([])
    visited.append([False])

for _ in range(M):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

cnt = 0
start = 1
stack = [start]
visited[1] = False
while stack:
    cur = stack.pop()
    for i in graph[cur]:
        if visited[i] is not False:
            stack.append(i)
            visited[i] = False
            cnt += 1
print(cnt)
