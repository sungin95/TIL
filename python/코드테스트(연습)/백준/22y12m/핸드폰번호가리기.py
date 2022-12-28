def solution(phone_number):
    a = len(phone_number)
    answer = ""
    for i in range(a - 4):
        answer += "*"
    else:
        answer += phone_number[-4:]
    return answer
