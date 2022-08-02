T = int(input())
for t in range(T):
    __ = int(input())
    M1_dict = {}
    answer = []
    M1 = list(map(int, input().split()))
    for i in M1:
        M1_dict[i] = 0
    ___ = int(input())
    M2 = list(map(int, input().split()))
    for j in M2:
        if M1_dict.get(j) == None:
            answer.append(0)
        else:
            answer.append(1)
    for ans in answer:
        print(ans)
