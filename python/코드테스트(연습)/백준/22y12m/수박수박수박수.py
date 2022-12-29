def solution(n):
    watermelon = "수박"
    N = n // 2
    M = n % 2
    answer = ""
    for i in range(N):
        answer += watermelon
    if M == 1:
        answer += watermelon[0]

    return answer
