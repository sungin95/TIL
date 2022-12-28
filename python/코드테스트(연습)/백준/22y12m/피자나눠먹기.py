def solution(n):
    cnt = 0
    while True:
        cnt += 1
        if (n * cnt) % 6 == 0:
            answer = (n * cnt) // 6
            break
    return answer
