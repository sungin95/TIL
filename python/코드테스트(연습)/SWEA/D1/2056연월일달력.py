import sys
sys.stdin = open("2056.txt", "r")
T = int(input())
for test_case in range(1, T + 1):
    d = input()
    if test_case % 2 == 0:
        print(f"#{test_case} -1")
        continue
    print(f"#{test_case} {d[0:4]}/{d[4:6]}/{d[6:8]}")