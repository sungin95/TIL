# 궁금한건 변수명을 opposite_pair, dice_list_pairs 등 매우 길게 했는데. 
# 이게 가독성을 오히려 떨어트리는건 아닌가 다른 분들의 의견이 궁금하다. 

# 문제 접근
# 주사위가 쌍이 있다는 것을 발견 했습니다. 
# 그래서 그걸 바탕으로 문제를 풀었습니다.  
from pprint import pprint


N = int(input())
answer_list = []
dice_list = []
dice_list_pairs = []
for __ in range(N):
    A,B,C,D,E,F = map(int, input().split())

    dice = [A,F,B,D,C,E] # 보기 편하게 순서를 좀 바꾸어 주었습니다. 
    dice_list.append(dice) # 일반 리스트 

    dice_pairs = [[A,F],[B,D],[C,E]] 
    dice_list_pairs.append(dice_pairs) # 쌍으로 된 리스트
pprint(dice_list)
"""
 [[2, 4, 3, 6, 1, 5], 첫번쨰 주사위
 [3, 5, 1, 4, 2, 6], 두번째 주사위
 [5, 2, 6, 1, 4, 3], 세번째 주사위
 [1, 5, 3, 2, 6, 4], 네번째 주사위
 [4, 3, 1, 5, 6, 2]] 다섯번째 주사위
 """
pprint(dice_list_pairs)
"""
[[[2, 4], [3, 6], [1, 5]], 첫번쨰 주사위
 [[3, 5], [1, 4], [2, 6]], 두번째 주사위
 [[5, 2], [6, 1], [4, 3]], 세번째 주사위
 [[1, 5], [3, 2], [6, 4]], 네번째 주사위
 [[4, 3], [1, 5], [6, 2]]] 다섯번째 주사위
"""
for i in range(1,7): # 주사위가 1에서 시작했을때, 2에서 시작했을때... 6에서 시작했을때 
    opposite_pair_list = [i] # 맨 밑에 값
    opposite_pair = i # 맨 밑에값에 반대면 수 알기 위해 초기 설정
    for j in range(N): # j는 쌓아 올린 주사위 수를 나타냈습니다. 
        location = dice_list[j].index(opposite_pair) # location는 위치 중요한 정보 X
        opposite_pair = dice_list_pairs[j][location//2][(location+1)%2] # [번째][몇번째 쌍인지][그중 앞인지 뒤인지]
        opposite_pair_list.append(opposite_pair) # [1, 5, 3, 4, 6, 2] [1, 5] [3, 5] [4, 3] [6, 4] [6, 2] 
    answer = []
    for j in range(1,N+1):
        set_dice = {1,2,3,4,5,6}
        set_b = {opposite_pair_list[j-1],opposite_pair_list[j]} # 세트 차집합을 이용해 주사위 옆면값을 알아내고 
        answer.append(max(set_dice ^ set_b)) # 그중 맥스
    answer_list.append(sum(answer))
print(max(answer_list))


