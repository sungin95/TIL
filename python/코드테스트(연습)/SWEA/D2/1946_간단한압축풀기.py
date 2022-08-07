T = int(input())
for t in range(T):
    N = int(input())
    original = ""
    for n in range(N):
        a, b = input().split()
        original += a*int(b)
    K = len(original)
    print(f"#{t+1}")
    for k in range(K):
        if k != 0:
            if k % 10 == 0:
                print()
        print(original[k],end="")
    else:
        print()