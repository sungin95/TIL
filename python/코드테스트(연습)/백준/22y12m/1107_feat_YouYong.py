import sys

sys.stdin = open("1107.txt", "r")

N = int(input())
a = int(input())
if a != 0:
    breakdown = set(input().split())
else:
    breakdown = set()

answer_list = [abs(100 - N)]


for i in range(1000000):
    if set(str(i)) & breakdown == set():
        answer_ = abs((N - i)) + len(list(str(i)))
        answer_list.append(answer_)

print(min(answer_list))
