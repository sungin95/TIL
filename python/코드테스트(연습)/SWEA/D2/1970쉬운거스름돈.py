import sys
sys.stdin = open("1970.txt", "r")
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    bank_note_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    result_ = 0
    print(f"#{test_case}")
    for money in bank_note_list:
        result_ = N // money
        N = N - (result_ * money)
        print(result_, end=" ")
    print("")