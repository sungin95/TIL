N = int(input())
i = 0
answer_list = []
N2 = N
while N2:
    answer = [N,N2]
    N2 -= 1
    while True:
        if answer[-2]-answer[-1] >= 0:
            answer.append(answer[-2]-answer[-1])
        else:
            answer_list.append([len(answer),answer])
            break
print(max(answer_list)[0])
print(*max(answer_list)[1])