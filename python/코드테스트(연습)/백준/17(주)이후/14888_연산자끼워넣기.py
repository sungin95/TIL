from collections import deque
import sys
sys.stdin = open("14888.txt", "r")


n = input()
num = deque(map(int, input().split()))
A, B, C, D = map(int, input().split())
answer_list = []
division_list = []
visited = [False] * (N+1)
addition = ['a'] * A
subtraction = ['b'] * B
multiplication = ['c'] * C
division = ['d'] * D


def dfs():
    pass


dfs()
print(addition, subtraction, multiplication, division)
print(num)
print(answer_list)
# print(max(list(answer_list)))
# print(min(list(answer_list)))
