import sys

sys.stdin = open("12869.txt", "r")

N = int(input())
scv = list(map(int, input().split()))
scv.sort(reverse=True)
min_attack_cnt = [100]


def min_attack_n2(scv, attack2, cnt):
    if min_attack_cnt[0] <= cnt:
        return
    cnt += 1
    for i in range(2):
        scv[0] -= attack2[i][0]
        scv[1] -= attack2[i][1]
        if 0 < scv[0] and 0 < scv[1]:
            min_attack_n2(scv, attack2, cnt)
        elif 0 < scv[0] or 0 < scv[1]:
            scv_one = max(scv)
            if scv_one % 9 == 0:
                c = scv_one // 9
            else:
                c = (scv_one // 9) + 1
            if min_attack_cnt[0] > cnt + c:
                min_attack_cnt[0] = cnt + c
        else:
            if min_attack_cnt[0] > cnt:
                min_attack_cnt[0] = cnt
        scv[0] += attack2[i][0]
        scv[1] += attack2[i][1]


def min_attack_n3(scv, attack3, attack2, cnt):
    if min_attack_cnt[0] <= cnt:
        return
    cnt += 1
    for i in range(6):
        scv[0] -= attack3[i][0]
        scv[1] -= attack3[i][1]
        scv[2] -= attack3[i][2]
        if 0 < scv[0] and 0 < scv[1] and 0 < scv[2]:
            min_attack_n3(scv, attack3, attack2, cnt)
        elif (
            (0 < scv[0] and 0 < scv[1])
            or (0 < scv[2] and 0 < scv[0])
            or (0 < scv[1] and 0 < scv[2])
        ):
            ssccvv = scv.copy()
            ssccvv.sort(reverse=True)
            min_attack_n2(ssccvv, attack2, cnt)
        elif 0 < scv[0] or 0 < scv[1] or 0 < scv[2]:
            scv_one = max(scv)
            if scv_one % 9 == 0:
                c = scv_one // 9
            else:
                c = (scv_one // 9) + 1
            if min_attack_cnt[0] > cnt + c:
                min_attack_cnt[0] = cnt + c
        else:
            if min_attack_cnt[0] > cnt:
                min_attack_cnt[0] = cnt
        scv[0] += attack3[i][0]
        scv[1] += attack3[i][1]
        scv[2] += attack3[i][2]


attack2 = [[9, 3], [3, 9]]
attack3 = [[9, 3, 1], [9, 1, 3], [3, 9, 1], [1, 9, 3], [1, 3, 9], [3, 1, 9]]
if N == 1:
    if scv[0] % 9 == 0:
        print(scv[0] // 9)
    else:
        print((scv[0] // 9) + 1)
elif N == 2:
    min_attack_n2(scv, attack2, 0)
    print(min_attack_cnt[0])
elif N == 3:
    min_attack_n3(scv, attack3, attack2, 0)
    print(min_attack_cnt[0])
    # print(scv)
