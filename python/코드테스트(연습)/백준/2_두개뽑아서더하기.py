# https://school.programmers.co.kr/learn/courses/30/lessons/68644
def solution(numbers):
    N = len(numbers)
    answer = []
    for i in range(N):
        for j in range(N):
            if i != j: # 서로 다른 인덱스일때 실행
                sum = numbers[i] + numbers[j]
                if sum not in answer: # 중복 방지
                    answer.append(sum)
    answer.sort() # 오름차순
    return answer


print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))
