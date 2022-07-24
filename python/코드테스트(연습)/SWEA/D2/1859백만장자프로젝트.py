# # 접근법: 그냥 MAX를 찾고 이전값은 더하고 다시 반복하고 그리고 끝내면 끝 아닌가?
import sys
sys.stdin = open("1859.txt", "r")
T = int(input())
for test_case in range(1, T + 1):
    n2 = int(input()) # 쓸모없이 이걸 왜 줬는지 모르겠다

    N = list(map(int, input().split()))
    print(n2)
    profit = 0
    while N != []: # 
        n = len(N)
        MAX_list = sorted(N)
        MAX = MAX_list[-1]
        print(MAX)
        MAX_i = 0 # MAX 위치
        for i in range(n): # 맥스를 찾는다. 
            if MAX == N[i]:
                MAX_i = i + 1
        for i in range(MAX_i): # 물건을 판다. 
            profit += (MAX - N[i])
        for i in range(MAX_i): # 지난간 날짜를 삭제한다. 
            N.pop(0)
        print(profit)
    print(f'#{test_case} {profit}')

# 아니 무슨 백만개가 넘어가냐.... 너무 한거 아닌가?