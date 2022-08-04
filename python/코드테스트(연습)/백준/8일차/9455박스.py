# 종이를 계속 끄적이다가 행렬을 90도 회전시키고 
# 이동거리 = 위치인덱스 - 상자 갯수
# 이걸 찾고 문제를 풀었습니다.   

T = int(input())
answer_list = []
for _ in range(T):
    N,M = map(int, input().split())
    grid_box_yx = []
    for n in range(N):
        box = list(map(int, input().split()))
        grid_box_yx.append(box)
    grid_box_xy = []
    for y in range(M):
        list_box = []
        for x in range(N-1,-1,-1): # 위치 인덱스를 이용하기 편하게 하기 위해 역수
            list_box.append(grid_box_yx[x][y])
        grid_box_xy.append(list_box) # 여기까지 행렬 바꾸기 과정.


    answer = 0 
    cnt = 0 # 상자갯수
    distance = 0 # 거리
    for x in grid_box_xy:
        Y = len(x)
        for i in range(Y):
            if x[i] == 1: # 1을 만나면
                distance += (i-cnt) # 거리 추가
                cnt += 1 # 상자갯수 추가 
        else: # 계산이 끝나면 
            answer += distance # 마지막 거리 추가 못한거 추가  
            cnt = 0 # 초기화 
            distance = 0 # 초기화

    answer_list.append(answer) # 정답 모으기
for ans in answer_list:
    print(ans) # 정답 출력
