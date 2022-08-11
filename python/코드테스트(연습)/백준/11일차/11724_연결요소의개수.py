# 그래프를 표현할 때
# 보통 노드들과 각각의 연결여부로 주어지는 경우가 많습니다.
# 보통 하나의 그래프라고하면
# 노드들이 각각 연결되어있는 것을 말하는데
# 실제로 그래프 정보를 받을 때 모든 노드가 연결되어 있지 않을 때가 있습니다.
# 그런 경우 각각의 그래프를 연결요소라고 표현합니다.
# 튜터님이 문제를 이해 못한 나를 위해 해준 해석ㅎㅎ
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
graph = []
first_line = []
for _ in range(N+1):
    graph.append([])

for m in range(M):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

answer_list = []

for start in range(1,N+1):
    stack = [start]
    visited = [False] * (N+1)
    visited2 = [start] # 들어간 요소를 리스트로 만들고 싶었습니다. 
    visited[start] = True
    while stack:
        cur = stack.pop()
        for adj in graph[cur]:
            if not visited[adj]:
                visited[adj] = True
                visited2.append(adj)
                stack.append(adj)    # 여기까지는 바이러스와 비슷합니다. 
    visited2.sort()
    answer_list.append(visited2) # 그 요소 리스트를 append
print(answer_list) # 결과 [[1, 2, 5], [1, 2, 5], [3, 4, 6], [3, 4, 6], [1, 2, 5], [3, 4, 6]]
answer = []
for ans in answer_list: # 위에 리스트들의 맨앞 한자리만 append를 해 갯수를 셈니다. 
    if ans[0] not in answer:
        answer.append(ans[0])
print(len(answer)) # 정답 제출