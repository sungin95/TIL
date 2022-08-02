import heapq
import sys
input = sys.stdin.readline
# 우선 이 문제가 어려웠던 이유는 절대값 때문이라고 생각합니다. 
# 힙 함수를 짜야 하는데. 절대값이 낮은 값을 출력해야 하는데. 자꾸 음수의 제일 낮은 값만 
# 출력이 되어서 힘들었다. 
# 이 문제를 해결하기 위해 2개의 통에 값을 담아야 한다고 생각을 하였다. 
T = int(input())
N_list = [] # 그 첫번째가 리스트.
# 우선 리스트에 해당 값을 절대값을 주어 저장을 한다. 
# 힙을 이용해 최소값을 빼 준다. (abs_min = 0)(여기까지는 우리가 아는 내용.) 
N_dict = {} # 그 두번째가 딕셔너리.
# 딕셔너리의 용도: 현재 딕셔너리에는 모든 값들이 카운터가 되어 있는 상태이다. 
# 예시) {-2: 5, -1: 0, 1: 0, 2: 3, 3: 2}식으로 
# 여기서 리스트에서 제일 낮은 1을 빼 주면. 문제 예시를 보면 -1이 우선적으로 나오는 것을 볼 수 있다.
# ! 관련코드
# 그래서 키가 -1인 값을 역카운트 해 주었다. 
# 그리고 키 값이 0이 되면 이젭부터 1을 역카운트 하게 만들어 주었다.    
abs_min = 0
answer = []
for _ in range(T):
    num = int(input())
    if num == 0: # 문제에서 0일때 출력한다고 했다. 
        if N_list == []:
            answer.append(0) # * 정답 모으기
        else:
            abs_min = heapq.heappop(N_list) # 가장 낮은 절대값. # 딕셔너리에 -abs_min 값을 우선적으로 역카운트 해 준다. 딕셔너리는 0이 되면 역카운트를 멈추게 한다. 
            if N_dict.get(-abs_min) == 0 or N_dict.get(-abs_min) == None:# ! 음수의 값이 카운트를 다 하거나 없으면 => 양수 역카운트 
                N_dict[(abs_min)] -= 1
                answer.append(abs_min) # * 정답 모으기
            else: # ! 음수가 남아 있으면 역카운트 
                N_dict[-abs_min] -= 1
                answer.append(-abs_min) # * 정답 모으기
    else: # 0이 아닐때 
        heapq.heappush(N_list, abs(num)) # 리스트에 푸쉬.
        
        if N_dict.get(num) == None: # 딕셔너리에 카운터 
            N_dict[num] = 1
        else:
            N_dict[num] += 1
for ans in answer: # * 정답 모으기
    print(ans)


    