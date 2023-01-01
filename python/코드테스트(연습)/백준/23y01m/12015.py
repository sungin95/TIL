# 첫 골2문제... 설렌다. 나도 과연 풀 수 있을까???
# import sys

# sys.stdin = open("12015.txt", "r")

t = int(input())
arr = list(map(int, input().split()))


def max_len(start, end, max_):

    max_list = [[start, arr[start], "up"]]
    min_list = [[start, arr[start], "down"]]

    for i in range(start, end):
        if arr[i] > max_list[-1][1]:
            max_list.append([i, arr[i], "up"])
        elif arr[i] < min_list[-1][1]:
            min_list.append([i, arr[i], "down"])

    sum_list = max_list + min_list[1:]
    sum_list.sort()

    for i in range(len(sum_list)):
        if sum_list[i][2] == "up":
            max_ += 1
        else:
            for j in range(i, len(sum_list)):
                if sum_list[j][2] == "up":
                    max___ = max_len(sum_list[i][0], sum_list[j][0] + 1, 0) - 1
                    if max_ < max___:
                        max_ = max___
                    break
    # print(sum_list, start, end)
    # print(max_, "max_")
    return max_


start = 0
end = len(arr)
max_ = 0
answer = max_len(start, end, max_)
print(answer)
