def solution(n, lost, reserve):
    lost_ = set(lost)
    reserve_ = set(reserve)
    aa = lost_ & reserve_
    for a in aa:
        lost.remove(a)
        reserve.remove(a)
    cnt = [n - len(lost)]

    def max_return(lost, reserve):
        for l in lost:
            ll = l + 1
            if ll in reserve:
                lost.remove(l)
                reserve.remove(ll)
                max_return(lost, reserve)
                if cnt[0] < n - len(lost):
                    cnt[0] = n - len(lost)
                lost.append(l)
                reserve.append(ll)
            ll = l - 1
            if ll in reserve:
                lost.remove(l)
                reserve.remove(ll)
                max_return(lost, reserve)
                if cnt[0] < n - len(lost):
                    cnt[0] = n - len(lost)
                lost.append(l)
                reserve.append(ll)

    max_return(lost, reserve)
    answer = cnt[0]
    return answer
