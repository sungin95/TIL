def solution(n):
    # 소수 디셔너리
    prime_number = {}

    answer = 0
    for i in range(2, n + 1):
        # 소수 디셔너리키값이 없으면 카운트
        if prime_number.get(i) == None:
            prime_number[i] = 1
            answer += 1
            cnt_ = 0
            #
            while True:
                cnt_ += 1
                i_ = i * cnt_
                if i_ <= n:
                    prime_number[i_] = 1
                else:
                    break

    return answer


# def solution(n):
#     a = [True] * (n + 1)
#     m = int(n**0.5)

#     for i in range(2, m + 1):
#         if a[i]:
#             for j in range(i + i, n + 1, i):
#                 a[j] = False
#     cnt = 0
#     for i in range(2, n+1):
#         if a[i]:
#             cnt += 1
#     return cnt


# def solution(n):
#     # 소수는 1과 본인의 수만 나눠지는 수 N제곱근보다 작은 수 중   N제곱근의 약수가 없다면 N의 약수도 없음
#     answer = 0
#     for j in range(2, n + 1):
#         check = 0
#         for i in range(2, int(j ** (1 / 2) + 1)):
#             if j % i == 0:
#                 check += 1
#                 break
#         if check == 0:
#             answer += 1
#     return answer
