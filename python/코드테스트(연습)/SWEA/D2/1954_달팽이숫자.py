T = int(input())
answer_final = []
for _ in range(T):
    N = int(input())
    snail_dict = {} # 리스트를 사용하면 [i][j]값이 없거나, 이미 값을 넣어줬으면 방향을 바꾸어야 하는데
    # 이때 [i][j]값이 없을때 에러가 나서 불편했습니다. 
    # 이때 딕셔너리.get을 사용하면 위 조건을 해결할 수 있기 떄문에 딕셔너리를 사용했습니다. 
    for i in range(N):
        for j in range(N):
            snail_dict[(i,j)] = 0 # N크기의 리스트 좌표를 키로 해서 각각 0을 넣어준다. 

    a = 0 # 좌표
    b = 0 # 좌표 (a,b)
    turn = 0 # 방향이 바뀔때 마다 1씩 증가, 움직이는 방향을 a -> b, b -> a 로 바꾸고 
    # 방향이 2번 바뀌면 a,b가 1씩 감소
    turn_2x = 0 # 방향이 연속 2번 바뀌면 brake
    value_ = 0 
    while True:
        if snail_dict.get((a,b)) == 0: # ! 달팽이 모양으로 움직이면 
            value_ += 1
            snail_dict[(a,b)] = value_ # 그에 해당하는 값을 대입(1,2,3...)
            turn_2x = 0 # 방향이 바뀌지 않으면 0으로 초기화 

        else: # ! 이미 지나간 곳을 만나거나, N*N을 벗어나면 (a,b)위치를 이전으로 돌려놔야 한다. 
            if (turn//2)%2 == 0: # 두번 바뀐횟수가 짝수(0포함)이고 # ! 아래 공통의 반대 
                if turn % 2 == 0: # 방향 바뀐 횟수가 짝수(0포함)일때 
                    b -= 1
                else: # 홀수 있때. 
                    a -= 1
            else: # 두번 바뀐횟수가 홀수이고
                if turn % 2 == 0: # 방향 바뀐 횟수가 짝수 
                    b += 1
                else: # 홀수 일때
                    a += 1

            turn += 1 # 값 1 증가 
            turn_2x += 1 # 연속으로 방향이 바뀐 횟수
            if turn_2x == 2: # 연속2번이면 계산 종료
                break
        
        if (turn//2)%2 == 0: # ! 공통 a혹은b +1혹은 -1
            if turn % 2 == 0:
                b += 1
            else:
                a += 1
        else:
            if turn % 2 == 0:
                b -= 1
            else:
                a -= 1

    answer = []
    for i in range(N): # 딕셔너리로 만든것을 리스트로 옮겨준다. 
        answer_list = []
        for j in range(N):
            answer_list.append(snail_dict[i,j]) 
        answer.append(answer_list) # 정답 모으기
    answer_final.append(answer) # 정답 모으기

t = 0
for ans2 in answer_final: # 정답 출력
    t += 1
    print(f"#{t}")
    for ans in ans2:
        print(*ans)
