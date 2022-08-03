# 접근법: 현재 인덱스와 이전 인덱스의 높이 차가 플러스면 올라는 중이고 마이너스이면 내려가는 중이다. 

n = int(input())
height = list(map(int, input().split()))

difference = 0 # 높이차
difference_list = [] # 높이차 모음
for i in range(1,n):
    if (height[i]-height[i-1]) > 0: # 높이차 플러스면 차이를 합친다. 
        difference += (height[i]-height[i-1])
    else:
        difference_list.append(difference) # 높이차가 음수면 합친값을 리스트에 넣고 
        difference = 0   # 차이는 초기화 
if max(height) == height[-1]: # 마지막이 max이면 그 값을 리스트에 못 넣는 예외가 발생하여 따로 해결 
    difference_list.append(difference)
print(max(difference_list)) # 차이의 최대치 print