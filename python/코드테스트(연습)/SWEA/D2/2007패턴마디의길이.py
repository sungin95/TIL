import sys
sys.stdin = open("2007.txt", "r")
T = int(input())
for test_case in range(1, T + 1):

    string_ = input()
    pattern_front = ""

    cnt = 0
    for i in range(1,30):
        if string_[cnt] == string_[i]:
            cnt += 1
        else:
            cnt = 0
    print(f'#{test_case} {30 - cnt}')

