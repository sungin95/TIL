import sys

sys.stdin = open("12015.txt", "r")

N = int(input())
arr = list(map(int, input().split()))

max_list = [(arr[0], 1)]

for i in range(1, N):
    max_list_check = []
    max_check = 0
    print(max_list)
    for ch in max_list:
        if ch[0] < arr[i]:
            if max_check < ch[1]:
                max_check = ch[1]
        else:
            max_list_check.append(ch)
    else:
        max_list = []
        for j in max_list_check:
            max_list.append(j)
        max_list.append((arr[i], max_check + 1))
# print(max_list)
answer_list = []
for an in max_list:
    answer_list.append(an[1])
print(max(answer_list))
