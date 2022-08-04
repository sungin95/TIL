import heapq
T = int(input())
answer_list = []
for _ in range(T):
    numbers = list(map(int, input().split()))
    
    numbers_minus = []
    for num in numbers: # max를 사용 할 수 있었지만 heapq을 사용해 보고 싶어서 모든 수를 음수화 하였습니다. 
        numbers_minus.append(-num) # heapqpop은 최소값만 출력할 수 있으니까 

    heapq.heapify(numbers_minus)
    for i in range(3):  # heappop과정 3번 반복하여 3번째 큰 수 출력. 
        max_third = heapq.heappop(numbers_minus)

    answer_list.append(-max_third) # 정답 모으기
for ans in answer_list:
    print(ans)

