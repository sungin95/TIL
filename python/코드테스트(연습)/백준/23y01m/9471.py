import sys

sys.stdin = open("9471.txt", "r")

m = int(input())
check_list = []
for i in range(m):
    data1, data2 = map(int, input().split())
    check_list.append([data1, data2])

fibo_check = [[]] * (m + 1)
fibo = [0, 1]
for i in range(510000):
    a = fibo[i - 1] + fibo[i]
    fibo.append(a)

answer_list = []
for i in range(m):
    ch = check_list[i][1]
    for fi in range(2, 510000):
        if (fibo[fi] % ch) == 0 and (fibo[fi + 1] % ch) == 1:
            answer_list.append(fi)
            break
print(answer_list)
