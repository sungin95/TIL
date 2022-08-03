# 이 문제는 딕셔너리를 이용하여 M1에 있는건 0, M2에 있는건 1을 입력하는 도중 
# 그 값이 없어 None이면 프린트 0을 값이 있으면 1을 입력해 주는 프로그램이다. 


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
