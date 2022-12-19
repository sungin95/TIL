N = int(input())
cnt = 0
cnt_list = [10000000]
dict_ = {}


def min_N(N, cnt):
    if cnt > min(cnt_list):
        return cnt

    cnt += 1
    if (N % 3) == 0:
        N_ = N // 3

        if dict_.get(N_) == None:
            dict_[N_] = cnt
        elif dict_[N_] + 1 >= cnt:
            dict_[N_] = cnt
        else:
            return

        if N_ == 1:
            if cnt < min(cnt_list):
                cnt_list.append(cnt)
            return cnt
        else:
            min_N(N_, cnt)

    if (N % 2) == 0:
        N_ = N // 2

        if dict_.get(N_) == None:
            dict_[N_] = cnt
        elif dict_[N_] + 1 >= cnt:
            dict_[N_] = cnt
        else:
            return

        if N_ == 1:
            if cnt < min(cnt_list):
                cnt_list.append(cnt)
            return cnt
        else:
            min_N(N_, cnt)
    N_ = N - 1

    if dict_.get(N_) == None:
        dict_[N_] = cnt
    elif dict_[N_] + 1 >= cnt:
        dict_[N_] = cnt
    else:
        return

    if N_ == 1:
        if cnt < min(cnt_list):
            cnt_list.append(cnt)
        return cnt
    else:
        min_N(N_, cnt)


if N == 1:
    print(0)
else:
    min_N(N, cnt)
    print(min(cnt_list))
