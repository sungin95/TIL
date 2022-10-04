import sys
sys.stdin = open("1206.txt", "r")
T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())

    arr = list(map(int, input().split()))

    dx = [-2,-1,1,2]
    dx_max = 0
    answer = 0
    for i in range(N):
        dx_list = []
        for j in range(4):
            if 0 <= i + dx[j] and i + dx[j] < N:
                dx_list.append(arr[i + dx[j]])
        else:
            dx_max = max(dx_list)
        if arr[i] > dx_max:
            answer += arr[i] - dx_max
    print(f"#{test_case}",answer)