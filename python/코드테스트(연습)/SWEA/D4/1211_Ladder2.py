import sys
sys.stdin = open("1210.txt", "r")

for t in range(1,11): # 10번의 테스트 케이스
    bored = []
    _ = input()
    for i in range(100):
        data = list(map(int, input().split()))
        bored.append(data) # 사다리 판 만들기 
    start_list = []
    for i in range(100):
        if bored[0][i] == 1:
            start_list.append(i) # 모든 시작 위치 경우의 수
    dx = [-1,1] # 좌우로 탐색 
    answer = 100000
    answer_list = []
    for start in start_list: # 각각의 사다리 출발
        answer_list.append(start) # 뒤의 pop랑 같이 쓰여서 cnt가 최소값을 갱신 할 때만 남는다. 결과적으로 answer_list[-1] 값이 최소값 x의 위치가 된다. 
        step = 0
        cnt = 0
        while True:
            if step == 99: # 끝에 도착하면 작동
                if answer > cnt: # 최소값 갱신
                    answer = cnt
                else:
                    answer_list.pop() # 필요없는 값 제거
                break
            check = False # 좌우 탐색하고 다시 반복하는 것을 방지하기 위해 만듬
            for i in range(2):
                if check == False:
                    while True:
                        nx = start + dx[i]
                        if 0 <= nx and nx < 100:
                            if bored[step][nx] == 1:
                                cnt += 1 # 최소 거리를 구할거면 옆으로 적게 가면 된다. 그래서 옆으로 가는 횟수만 세어 준다. 
                                start = nx # 줄 바꾸기 
                                check = True # 한쪽으로 이동하면 step을 이동한다. 
                            else:
                                break
                        else:
                            break
            else:
                step += 1 # 한칸씩 이동 
    print(f"#{t}",answer_list[-1])




            





