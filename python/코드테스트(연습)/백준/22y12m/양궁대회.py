# 정확성 66% 이 이상은 모르겠음
# 내가 생각하는 내 코드의 문제점
# 점수가 같다면 가장 낮은 점수 위주로 표현을 해야 하는데. 내가 만든 식은 가장 높은 값부터 표현을 하도록 설계가 되어있다.
# 아마 여기서 문제가 난거 같고, 이걸 바꿀려면 전체를 다시 짜야 되서 여기까지....


def solution(n, info):
    analysis = []
    # 상대방 점수는 마이너스로 계산
    my_score = 0
    for i in range(11):
        score = 10 - i
        if info[i] == 0:
            pass
        else:
            my_score -= score

    # 분석을 위한 틀 제작
    for i in range(11):
        score = 10 - i
        if info[i] == 0:
            analysis.append([score, score, 1, score])
        else:
            analysis.append(
                [(score * 2) / (info[i] + 1), score * 2, info[i] + 1, score]
            )  # 기대값 비교 ,점수 더하기, 화살갯수, 점수 찾기
    analysis.sort()
    analysis.reverse()

    # 계산
    answer = []
    for ana in analysis:

        if n >= ana[2]:
            n -= ana[2]
            my_score += ana[1]

            answer.append([ana[3], ana[2]])
        else:
            answer.append([ana[3], 0])
    else:
        if n != 0:
            answer[-1][1] = n

    answer.sort()
    answer.reverse()
    answer2 = []
    if my_score > 0:
        for i in answer:
            answer2.append(i[1])
    else:
        answer2 = [-1]
    print(my_score)
    print(analysis)
    print(answer)
    print(answer2)

    return answer2
