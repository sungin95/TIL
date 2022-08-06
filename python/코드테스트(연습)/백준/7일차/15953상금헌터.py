T = int(input())

answer = []
for _ in range(T):
    a, b = map(int, input().split())
    money = 0
    if a == 0:
        money = 0
    elif a == 1:
        money = 5000000
    elif a <= 3:
        money = 3000000
    elif a <= 6:
        money = 2000000
    elif a <= 10:
        money = 500000
    elif a <= 15:
        money = 300000
    elif a <= 21:
        money = 100000
    money2 = 0
    if b == 0:
        money2 = 0
    elif b <= 1:
        money2 = 5120000
    elif b <= 3:
        money2 = 2560000
    elif b <= 7:
        money2 = 1280000
    elif b <= 15:
        money2 = 640000
    elif b <= 31:
        money2 = 320000
    answer.append(money + money2)

for ans in answer:
    print(ans)