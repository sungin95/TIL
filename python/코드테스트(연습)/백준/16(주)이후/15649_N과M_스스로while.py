from copy import copy

a, b = map(int, input().split())
save = []
arr = []
for i in range(b):
    save.append([])
answer_list = []
if b == 1:
    for i in range(1, a+1):
        print(i)


else:
    for i in range(b):
        for j in range(a, 0, -1):
            if j not in arr:
                save[i].append(j)
        else:
            A = save[i].pop()
            arr.append(A)
    else:
        A = arr.pop()
        save[-1].append(A)
    while save[-1] != []:
        A = save[-1].pop()
        arr.append(A)
        A = copy(arr)
        arr.pop()
        answer_list.append(A)

    while True:
        k = -1
        while True:
            if save[k] == []:
                k -= 1
            else:
                break
        print(arr, save)
        for i in range(-k-1):
            arr[-i-1] = copy(save[-i-2][-1])
        print(arr, save)
        for i in range(b):
            if save[i] == []:
                for j in range(a, 0, -1):
                    if j not in arr:
                        save[i].append(j)
        save[k].pop()

        while save[-1] != []:
            A = save[-1].pop()
            arr.append(A)
            A = copy(arr)
            arr.pop()
            answer_list.append(A)
        if save[0] == []:
            break

    print(arr)
    print(save)
    print(answer_list)
