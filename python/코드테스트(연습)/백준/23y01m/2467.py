import sys

sys.stdin = open("2467.txt", "r")

from bisect import bisect_left

N = int(input())
num_list = list(map(int, input().split()))
num_list.sort()
min_ = 100000000000
min_list = []
for num in num_list:
    num2 = -num
    # bisect 를 사용하여 문제 풀이
    num__ = bisect_left(num_list, num2)
    # 값 이상
    if 0 <= num__ < len(num_list):
        num___1 = abs(num + (num_list[num__]))
        # 0 0 같은 경우 문제가 발생
        if num == num_list[num__]:
            for j in [-1, 1]:
                if 0 <= num___1 + j < len(num_list):
                    num___1 = abs(num + (num_list[num__ + j]))
                    if min_ > num___1:
                        min_ = num___1
                        min_list = [num, num_list[num__ + j]]

        elif min_ > num___1:
            min_ = num___1
            min_list = [num, num_list[num__]]
    # 값 이하
    num__11 = num__ - 1
    if 0 <= num__11 < len(num_list):
        if num == num_list[num__11]:
            for j in [-1, 1]:
                if 0 <= num__11 + j < len(num_list):
                    num___1 = abs(num + (num_list[num__11 + j]))
                    if min_ > num___1:
                        min_ = num___1
                        min_list = [num, num_list[num__11 + j]]

        elif num != num_list[num__11]:
            num___1 = abs(num + (num_list[num__11]))
            if min_ > num___1:
                min_ = num___1
                min_list = [num, num_list[num__11]]


min_list.sort()
answer = ""
for ans in min_list:
    answer += str(ans)
    answer += " "
print(answer)
