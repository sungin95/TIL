import sys
sys.stdin = open("4963.txt","r")
answer_list = []

while True:  
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    island_map = []
    for _ in range(M):
        data = input().split()
        island_map.append(data)
    nx = [-1,-1,-1, 0, 0, 1,1,1] # 델타탐색 이용.
    ny = [-1, 0, 1,-1, 1,-1,0,1]
    cnt = 0

    for y in range(M):
        for x in range(N):
            if island_map[y][x] == "1": #섬을 찾으면 시작
                island_map[y][x] = "0" # 우선 해당 점을 0으로 바꾸어 줍니다. 
                island_list = []
                island_list.append([y,x])
                y_same = y # 값 변형을 막기 위해 y,x 를 바꾸어 주었습니다. 
                x_same = x
                while True:
                    for n in range(8): # 델타 8방위 탐색
                        if 0 <= y_same+ny[n] and y_same+ny[n] < M and 0 <= x_same+nx[n] and x_same+nx[n] < N:
                            # 범위를 넘지 않으면 시행
                            if island_map[y_same+ny[n]][x_same+nx[n]] == "1":# 1을 찾으면
                                island_list.append([y_same+ny[n],x_same+nx[n]]) # 해당좌표 리스트에 저장 
                                island_map[y_same+ny[n]][x_same+nx[n]] = "0" # 0으로 바꾸어 준다. 
                    else: # 8방 탐색이 끝나면 
                        try:
                            a = island_list.pop() # 리스트에 저장한 요소 하나를 꺼내 줍니다. 
                            y_same = a[0] # 저장한 좌표를 대입하고 while문에 의해 다시 시작합니다. 
                            x_same = a[1] # 
                        except: # 더 이상 꺼낼게 없으면 
                            cnt += 1 # 카운터 
                            break # 위식 종류
    answer_list.append(cnt)
for ans in answer_list:
    print(ans)

