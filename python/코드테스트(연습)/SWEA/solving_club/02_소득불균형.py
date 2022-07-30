import sys
sys.stdin = open("02.txt", "r")
t = int(input())
for test_case in range(1, t + 1):
    n = int(input())
    incomes = list(map(int, input().split()))
    average = sum(incomes)//n
    cnt = 0
    for i in incomes:
        if average >= i:
            cnt += 1
    print(f"#{test_case} {cnt}")

