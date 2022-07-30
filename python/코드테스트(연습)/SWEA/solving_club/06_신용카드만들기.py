import sys
sys.stdin = open("06.txt", "r")
t = int(input())
for test_case in range(1, t + 1):
    N = input()
    make_card_able = 1
    if N[0] == "3" or N[0] == "4" or N[0] == "5" or N[0] == "6" or N[0] == "9":
        make_card_able = 1
    else:
        make_card_able = 0

    n_ = N.count("-")

    n = len(N)
    if n - n_ != 16:
        make_card_able = 0

    print(f"#{test_case} {make_card_able}")