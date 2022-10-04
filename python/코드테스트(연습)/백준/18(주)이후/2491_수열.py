n = int(input())
arr = list(map(int, input().split()))
arr_reverse = list(arr.__reversed__())

# print(arr)
# print(arr_reverse)

cnt_list = []
def bigger_and_bigger(arr):
    cnt = 0
    num = 0
    for i in range(n):
        if arr[i] >= num:
            num = arr[i]
            cnt += 1
        else:
            cnt_list.append(cnt)
            cnt = 1
            num = arr[i]
    else:
        cnt_list.append(cnt)
    return cnt_list
bigger_and_bigger(arr)
bigger_and_bigger(arr_reverse)

print(max(cnt_list))