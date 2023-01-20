def solution(N, stages):
    failure_rate = [0 for i in range(N + 2)]
    stages.sort()
    check = []
    num = 0
    cnt = 0
    for s in stages:
        if num != s:
            failure_rate[num] = (1, (len(stages) - cnt))
            num = s
            check = [s]
        else:
            check.append(s)
        cnt += 1
    else:
        failure_rate[num] = (1, (len(stages) - cnt + 1))
    print(failure_rate)
    answer = []
    return answer


solution(4, [4, 4, 4, 4, 4])
