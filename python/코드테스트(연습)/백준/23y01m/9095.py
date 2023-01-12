import sys

sys.stdin = open("9095.txt", "r")


answer_list = []
T = int(input())
for t in range(T):
    N = int(input())

    order_list = []

    def sum_cases(N, sum_, order):
        num_list = [1, 2, 3]
        for i in num_list:
            sum_ += i
            order += str(i)
            if N <= sum_:
                if N == sum_:
                    order_list.append(order)
                return
            else:
                sum_cases(N, sum_, order)
                sum_ -= i
                order[:-1]

    order = ""
    sum_cases(N, 0, order)

    answer_list.append(len(order_list))
for answer in answer_list:
    print(answer)
