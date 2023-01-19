import sys

sys.stdin = open("9461.txt", "r")

T = int(input())
answer_list = []
for t in range(T):
    N = int(input())
    t_num = [1, 1, 1, 2, 2]
    if N == 1:
        answer_list.append(1)
    elif N == 2:
        answer_list.append(1)
    elif N == 3:
        answer_list.append(1)
    elif N == 4:
        answer_list.append(2)
    elif N == 5:
        answer_list.append(2)
    else:
        for i in range(5, N):
            new = t_num[i - 1] + t_num[i - 5]
            t_num.append(new)
        answer_list.append(t_num[-1])
for answer in answer_list:
    print(answer)
