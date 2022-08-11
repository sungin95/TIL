N = int(input())
graph = []
for _ in range(N+1):
    graph.append([])
start,end = map(int, input().split())
M = int(input())
for _ in range(M):
    v1,v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)


stack = [start]
stack2 = []
cnt = 0
visited = [False] * (N+1)
visited[start] = True
unconnection = False # 연결이 안되어 있으면 끝내기 위한 장치
check = False # 촌수를 확인하면 종료.
while check == False:
    if unconnection == True: # 모두 돌아도 없으면 종료.
        cnt = -1
        break
    for a in stack2: # 받은 내용에 찾는 친척 있으면 종료.
        if a == end:
            check = True # 촌수를 확인하면 종료.
    if check == True:
        break
    unconnection = True # ! 만약 아래에서 False 안시키면 계산 종류
# ! 위식들은 연결이 되어 있지 않거나 촌수를 확인하면 종류가 되는 식입니다. 
# 깊게 한칸씩이 아니라 시작:[7] => [2] => [1, 7, 8] => [3]
#     ---9
# 1 -2 - 8
# ㅣ   - 7
# 3    
# 이런 구조를 만들기 위해 stack에다 stack2를 만들었습니다. 
    # print(stack2)
    cnt += 1
    for sta in stack2: # 여기서 stack2를 stack에게 전수해줍니다. 
        stack.append(sta)
    stack2 = [] # stack2 초기화
    while stack: 
        current = stack.pop()
        for adj in graph[current]:
            if not visited[adj]:
                visited[adj] = True
                stack2.append(adj) # 방문하지 않은 자리중 인접한 값들을 넣어줍니다. 
                unconnection = False # ! 인접한 값이 없으면 종료.
print(cnt)