T = int(input())
answer = []
for _ in range(T):
    N = int(input())
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    while N % 2 == 0:
        N = N // 2
        a += 1
    while N % 3 == 0:
        N = N // 3
        b += 1
    while N % 5 == 0:
        N = N // 5
        c += 1
    while N % 7 == 0:
        N = N // 7
        d += 1
    while N % 11 == 0:
        N = N // 11
        e += 1
    answer.append([a,b,c,d,e])
t = 0
for ans in answer:
    t += 1
    print(f"#{t}",end=" ")
    print(*ans)
