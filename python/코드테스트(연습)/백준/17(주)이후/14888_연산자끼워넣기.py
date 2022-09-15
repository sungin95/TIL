from copy import copy
import sys
sys.stdin = open("14888.txt", "r")

n = int(input())
num = list(map(int, input().split()))
A, B, C, D = map(int, input().split())
A_list = ['+']*A
B_list = ['-']*B
C_list = ['*']*C
D_list = ['//']*D
ABCD_list = [A_list, B_list, C_list, D_list]

arr = []

answer_list = []


def dfs():
    global answer
    global dp
    if len(arr) == n-1:
        answer = 0
        dp = copy(num[0])  # 중간 계산된 값을 저장하기 위해
        # print(*arr)
        for j in range(n-1):
            if arr[j] == '+':
                answer = dp + num[j+1]
                dp = copy(answer)
            elif arr[j] == '-':
                answer = dp - num[j+1]
                dp = copy(answer)
            elif arr[j] == '*':
                answer = dp * num[j+1]
                dp = copy(answer)
            elif arr[j] == '//':
                if dp >= 0:
                    answer = dp // num[j+1]
                    dp = copy(answer)
                else:
                    answer = -(abs(dp) // num[j+1])
                    dp = copy(answer)
        answer_list.append(answer)
        return
    else:
        for i in ['+', '-', '*', '//']:
            if i == '+':
                if arr.count(i) != A:
                    arr.append(i)
                    dfs()
                    arr.pop()
            if i == '-':
                if arr.count(i) != B:
                    arr.append(i)
                    dfs()
                    arr.pop()
            if i == '*':
                if arr.count(i) != C:
                    arr.append(i)
                    dfs()
                    arr.pop()
            if i == '//':
                if arr.count(i) != D:
                    arr.append(i)
                    dfs()
                    arr.pop()


dfs()
answer_list.sort()
print(answer_list[-1])  # 최댓값
print(answer_list[0])  # 최솟값
