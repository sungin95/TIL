# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")
T = int(input())
for i in range(T):
    cnt = 0
    score = 0
    O_X = input()
    for ox in O_X:
        if ox == "O":
            cnt += 1 # 1회 연속 1, 2연속 2, 3연속 3
            score += cnt
        else:
            cnt = 0 # 연속이 깨지면 초기화
    print(score)