def solution(numbers):
    N = len(numbers)
    answer = []
    for i in range(N):
        for j in range(N):
            if i != j:
                sum = numbers[i] + numbers[j]
                if sum not in answer:
                    answer.append(sum)
    answer.sort()
    return answer
