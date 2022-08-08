import heapq
T = int(input())
answer_list = []
for t in range(T):
    class_ = list(map(int, input().split()))
    class_score = class_[1:] # 필요 없는 거 맨앞에 제거 

    max_ = max(class_score) # 최대값
    min_ = min(class_score) # 최솟값

    heapq.heapify(class_score) # 점수차를 최소값들을 차례로 불러내 값 차이를 이용해 제거. 
    b = class_score[0] # 제일 첫번째값 점수차 0 만들기 위해. 
    gap_list = []
    while class_score != []:
        a = heapq.heappop(class_score) #a는 현재 최소값 b는 이전 최소값
        gap = a - b
        gap_list.append(gap)
        b = a
    answer_list.append([max_,min_,max(gap_list)])
t = 0
for ans in answer_list:
    t += 1
    print(f"Class {t}")
    print(f"Max {ans[0]}, Min {ans[1]}, Largest gap {ans[2]}")