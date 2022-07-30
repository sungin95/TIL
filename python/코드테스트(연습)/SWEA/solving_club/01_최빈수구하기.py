import sys
sys.stdin = open("01.txt", "r")
t = int(input())
for test_case in range(1, t + 1):
    ___ = int(input())

    N = map(int, input().split())
    score_dict = {}
    for i in N:
        if score_dict.get(i) == None:
            score_dict[i] = 1
        else: 
            score_dict[i] += 1

    most_frequent = 0
    mf_score = 0
    for j in range(101):
        if score_dict.get(j) != None:
            if score_dict[j] >= most_frequent:
                most_frequent = score_dict[j]
                mf_score = j

                
    print(f"#{test_case} {mf_score}")