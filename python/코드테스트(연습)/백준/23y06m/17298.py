import sys

sys.stdin = open("17298.txt", "r")

"""
문제 해결을 위해 스택 구조를 활용습니다. 
"""

N = int(input())
num_list = list(map(int, input().split()))
stack = list()
nge = [-1 for i in range(len(num_list))]

for i in range(len(num_list)):
    num = num_list[i]
    while stack and num_list[stack[-1]] < num:
        nge[stack.pop()] = num
    stack.append(i)
print(" ".join(map(str, nge)))
