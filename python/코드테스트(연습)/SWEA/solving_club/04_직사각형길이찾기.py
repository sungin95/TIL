import sys
sys.stdin = open("04.txt", "r")
t = int(input())
for test_case in range(1, t + 1):
    a, b, c = map(int, input().split())

    d = 0 
    if a == b:
        d = c
    elif a == c:
        d = b
    elif b == c:
        d = a

    print(f"#{test_case} {d}")