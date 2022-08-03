# 함수 max를 통해 max인 날짜를 찾으면 
# 그 이전 날까지 구매를 합니다. (buy_days)
# 그리고 맥스인 날에 모두 판매를 해 이익을 얻고(profit)
# 다시 맥스인 날을 구하고 
# 이전 맥스의 위치에 하루를 더한 위치부터 다시 물건을 사기 시작합니다. (MAX_i )
# 그리고 MAX_i 값이 끝에 오면 계산을 멈춥니다. 
import sys
sys.stdin = open("1859.txt", "r")
T = int(input())
for test_case in range(1, T + 1):
    n = int(input())  
    N_first = list(map(int, input().split()))
    MAX_i = 0 # MAX 위치
    over_days = 0 # 지나간 날들
    buy_days = 0 # 산 날들
    profit = 0 # 이익량
    while MAX_i != n: 
        N = N_first[MAX_i:] # MAX_i 위치부터 리스트를 다시 만듭니다. 
        MAX = max(N) 
        for i in range(n-MAX_i): # 맥스를 찾는다. (갯수는 전체 날짜에서 지나간 날짜를 빼 주었습니다.)
            if MAX == N[i]:
                MAX_i += i+1 # max값을 찾으면 그 다음 위치(인덱스)에 MAX_i로 지정합니다. 
                break # max위치를 찾으면 이 이상의 계산은 무의미하여 계산 과정을 줄이기 위해 넣었습니다. 
        buy_days = MAX_i - over_days # 물건은 사는 날은 새롭게 찾는 맥스의 위치(인덱스)값 - 이전 맥스에서 물건을 다 팔고 이익을 가져왔던 지나간 날들입니다. 
        for i in range(buy_days): #  물건을 판다.  
            profit += (MAX - N[i])
        over_days = MAX_i # 물건을 다 팔고 나면 현재 max까지의 날들은 지나간날( over_days)로 합니다. 
    print(f'#{test_case} {profit}')