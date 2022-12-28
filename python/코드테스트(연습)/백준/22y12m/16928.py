import sys

sys.stdin = open("16928.txt", "r")

N, M = map(int, input().split())

up_down_dict = {}
for _ in range(N + M):
    a, b = map(int, input().split())
    up_down_dict[a] = b

print(up_down_dict)

answer_list = []


def move(i, cnt):
    if i < 10:
        print(i, cnt)
        cnt += 1
        if up_down_dict.get(i) is not None:
            i = up_down_dict[i]
        for j in range(1, 7):
            k = i + j
            if k <= 10:
                move(k, cnt)
        return
    elif i == 10:
        answer_list.append(cnt)


move(1, 0)
print(answer_list)
