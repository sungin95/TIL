T = int(input())
for i in range(T):
    cnt = 0
    score = 0
    O_X = input()
    for ox in O_X:
        if ox == "O":
            cnt += 1
            score += cnt
        else:
            cnt = 0
    print(score)