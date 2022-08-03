import sys
sys.stdin = open("1966.txt", "r")

T = int(input())
str_ = ""
for test_case in range(1, T + 1):
    _ = input()
    N = sorted(map(int, input().split()))
    print(f"#{test_case}", end=" ")
    for n in N:
        print(n, end=" ")
    print()
        