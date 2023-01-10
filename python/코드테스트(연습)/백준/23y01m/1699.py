import math


N = int(input())

max_cnt = [1000001]


def case(N, N_root, cnt):
    M = N
    M_root = N_root
    cnt_ = 0
    while M:
        M_root = math.floor(math.sqrt(M))
        if M_root > N_root:
            M_root = N_root
        M -= M_root**2
        cnt_ += 1
        if cnt < cnt_:
            break
    if cnt > cnt_:
        cnt = cnt_
        max_cnt[0] = cnt_
    if N_root - 1 > 0:
        # print(N, N_root - 1, cnt)
        case(N, N_root - 1, cnt)


N_root = math.floor(math.sqrt(N))

case(N, N_root, 100001)
print(max_cnt[0])
