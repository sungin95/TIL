# 생각의 전환 문제
# M개씩 더하는게 아니라
# 맨 뒤에 값을 빼 주고 맨 앞에 값을 더해 주는 문제. 

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
temperature = list(map(int, input().split()))

first_value = sum(temperature[:M])
sum_list = [first_value]

for i in range(M,N):
    first_value += temperature[i]
    first_value -= temperature[i-M]
    sum_list.append(first_value)
print(max(sum_list))
