N, M = map(int, input().split())
K = int(input())
cnt = 0
cnt_2 = 1
cnt_2_minus = 0
location = [0,0]
if K <= (N*M):
    while True:
        if K <= 0:
            break
        cnt += 1
        cnt_2 += 1
        if cnt % 4 == 1:
            location = [M-(cnt//4),1+(cnt//4)]
            K -= M + cnt_2_minus
            if K <= 0:
                location[0] += K
        elif cnt % 4 == 2:
            location = [M-(cnt//4),N-(cnt//4)]
            K -= N + cnt_2_minus
            if K <= 0:
                location[1] += K
        elif cnt % 4 == 3:
            location = [1+(cnt//4),N-(cnt//4)]
            K -= M + cnt_2_minus
            if K <= 0:
                location[0] -= K
        elif cnt % 4 == 0:
            location = [(cnt//4),1+(cnt//4)]
            K -= N + cnt_2_minus
            if K <= 0:
                location[1] -= K
        if cnt_2 % 2 == 0:
            cnt_2_minus -= 1
else:
    print(0)
if location != [0,0]:
    print(location[1],location[0])

