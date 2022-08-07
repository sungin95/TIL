# M - N + 1
# 이 문제는 서로 다른 길이를 가진 두 리스트의 값을 서로 마주보는 값들 끼리 곱한 값중
# 가장 큰 값을 출력하는 문제입니다.
# 여기서 가장 번거로운것이 N과 M중 무엇이 더 긴지를 알 수 없다는 것입니다. 
# 그것을 알지 못하면 식을 짜는데 어려운이 큽니다. 
# 그래서 문제를 해결하기 위해 if else를 사용하여 무조건 M이 더 길게 만들었습니다. # !  
import sys
sys.stdin = open("1959.txt", "r")
T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    if N <= M:
        N_list = list(map(int, input().split()))
        M_list = list(map(int, input().split()))
    else: # ! N이 더 길면 N과 M 모두 값을 바꾸어 주었습니다. 
        q = N
        w = M
        M = q
        N = w
        M_list = list(map(int, input().split()))
        N_list = list(map(int, input().split()))

    A = M - N + 1 # 무조건 M이 크게 만들었으므로 A는 무조건 abs이다. 
    max_ = 0 # 정답
    max_list = [] # 후보군 sum_을 받을 예정
    for a in range(A):
        sum_ = 0 # 후보군 값
        for n in range(N):
            b = N_list[n] * M_list[n + a] 
            sum_ += b
        else: # 후보군을 모은다. 
            max_list.append(sum_)
    else: # 후보군중 가장 큰값 max_
        max_ = max(max_list)
    print(f"#{t+1} {max_}") 