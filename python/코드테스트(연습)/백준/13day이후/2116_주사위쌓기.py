N = int(input())
answer_list = []
dice_list = []
dice_list_pairs = []
for __ in range(N):
    A,B,C,D,E,F = map(int, input().split())

    dice = [A,F,B,D,C,E]
    dice_list.append(dice) # 일반 리스트 

    dice_pairs = [[A,F],[B,D],[C,E]] 
    dice_list_pairs.append(dice_pairs) # 쌍으로 된 리스트

for i in range(1,7):
    opposite_pair_list = [i]
    opposite_pair = i
    for j in range(N):
        location = dice_list[j].index(opposite_pair) # location는 위치 중요한 정보 X
        opposite_pair = dice_list_pairs[j][location//2][(location+1)%2] # opposite_pair
        opposite_pair_list.append(opposite_pair)

    answer = []
    for j in range(1,N+1):
        set_dice = {1,2,3,4,5,6}
        set_b = {opposite_pair_list[j-1],opposite_pair_list[j]} # 세트 차집합을 이용해 주사위 옆면값을 알아내고 
        answer.append(max(set_dice ^ set_b)) # 그중 맥스
    answer_list.append(sum(answer))
print(max(answer_list))


