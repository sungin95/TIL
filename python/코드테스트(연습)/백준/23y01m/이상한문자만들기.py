def solution(sss):
    ss = sss.split(" ")
    answer = ""
    for s in ss:
        for i in range(len(s)):
            if i % 2 == 0:
                answer += s[i].upper()
            else:
                answer += s[i].lower()
        else:
            answer += " "
    # strip은 왜 안되는 걸까?
    answer = answer[:-1]
    return answer
