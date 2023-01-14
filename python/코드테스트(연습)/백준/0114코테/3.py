import sys

sys.stdin = open("3.txt", "r")

N, M, C = map(int, input().split())

case__ = []
for i in range(C):
    data = list(map(int, input().split()))
    case__.append(data)

A = []
B = []

A = list(map(int, input().split()))

B = list(map(int, input().split()))


answer_list = []
if N < M:
    cnt = 0
    sum_ = 0
    for i in range((M - N) + 1):
        for j in range(N):
            AA = A[j]
            BB = B[j + cnt]
            sum_ += case__[AA - 1][BB - 1]
        cnt += 1
        answer_list.append(sum_)
        sum_ = 0
elif N > M:
    cnt = 0
    sum_ = 0
    for i in range((N - M) + 1):
        for j in range(M):
            AA = A[j + cnt]
            BB = B[j]
            sum_ += case__[AA - 1][BB - 1]
        cnt += 1
        answer_list.append(sum_)
        sum_ = 0
elif N == M:
    cnt = 0
    sum_ = 0
    for i in range(1):
        for j in range(M):
            AA = A[j]
            BB = B[j]
            sum_ += case__[AA - 1][BB - 1]
        cnt += 1
        answer_list.append(sum_)
        sum_ = 0
print(max(answer_list))
