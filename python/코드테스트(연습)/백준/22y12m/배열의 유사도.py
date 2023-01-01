def solution(s1, s2):
    s1 = set(s1)
    s2 = set(s2)
    s_answer = s1 & s2
    answer = len(s_answer)
    return answer
