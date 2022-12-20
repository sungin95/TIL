def solution(n, info):
    case = []
    max_ = 0
    # 자리수를 맞추기 위해 1024 ~ 2048
    for i in range(1024, 2048):

        # 1024가지의 라이온 경우의 수 중 1개
        lie_list = list(map(int, reversed(str(bin(i))[3:])))
        lie = 0
        api = 0

        # 화살갯수를 넘기면 넘기기 or 남으면 0에다 쏜걸로
        n_check = 0
        for j in range(10):
            if lie_list[j] == 1:
                n_check += info[j] + 1
        if n < n_check:
            continue
        else:
            lie_list.append(n - n_check)

        # 라이온과 어피치 점수 계산
        for j in range(10):
            if lie_list[j] == 1:
                lie += 10 - j

            elif info[j] != 0:
                api += 10 - j

        # 라이온이 어피치보다 점수가 높고, max값이 값거나 클때 case 업데이트
        if lie > api and lie - api >= max_:
            max_ = lie - api
            case = lie_list

    # case 의 값에 따라 정답을 출력하도록 작업
    answer = []
    if case == []:
        answer = [-1]
    else:
        for i in range(10):
            if case[i] == 0:
                answer.append(0)
            else:
                answer.append(info[i] + 1)
        else:
            answer.append(case[10])

    return answer
