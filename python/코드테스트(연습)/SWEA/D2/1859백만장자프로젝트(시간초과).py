# # 접근법: 그냥 MAX를 찾고 이전값은 더하고 다시 반복하고 그리고 끝내면 끝 아닌가?
import sys
sys.stdin = open("1859.txt", "r")
T = int(input())
for test_case in range(1, T + 1):
    n = int(input()) # 이것도 활용해야 겠네. 
    N_first = list(map(int, input().split()))
    MAX_i = 0 # MAX 위치=> # ! 범위로 고쳐야 한다. 
    over_days = 0
    buy_days = 0
    profit = 0
    while MAX_i != n: 
        N = N_first[MAX_i:]
        MAX = max(N) # 이렇게 좋은게 있구나
        for i in range(n-MAX_i): # 맥스를 찾는다. 
            if MAX == N[i]:
                MAX_i += i+1 
                break 
        buy_days = MAX_i - over_days
        for i in range(buy_days): #  물건을 판다.  
            profit += (MAX - N[i])
        over_days = MAX_i
    print(f'#{test_case} {profit}')
    
# 아무리 봐도 코드에 문제가 없는데. runtimeerror가 뜬다. 이유를 모르겠다. 