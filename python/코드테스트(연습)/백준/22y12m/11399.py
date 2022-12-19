_ = int(input())
N_list = list(map(int, input().split()))
sum_ = 0
answer = 0
N_list.sort()
for N_ in N_list:
    sum_ += N_
    answer += sum_
print(answer)
