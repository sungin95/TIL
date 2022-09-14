from collections import deque
import sys
sys.stdin = open("14888.txt", "r")


n = input()
num = deque(map(int, input().split()))
addition, subtraction, multiplication, division = map(int, input().split())
answer_list = []
division_list = []


def dfs():
    global addition
    global subtraction
    global multiplication
    global division
    if len(num) == 1:
        answer_list.append(num[0])
        return
    else:
        for i in [addition, subtraction, multiplication, division]:
            if i != 0:
                pass


dfs()
print(num)
print(answer_list)
print(max(list(answer_list)))
print(min(list(answer_list)))
