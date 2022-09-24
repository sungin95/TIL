N, K = map(int, input().split())

if N == 0 or K == 0:
    print(abs(N-K))
elif N >= K:
    print(abs(N-K))
else:
    cnt = 0
    while N != K:
        print(N, K)
        if 2*N <= K:
            N = 2*N
            cnt += 1
        elif 2*N == (K-1):
            cnt += 2
            break
        elif N < K:
            N += 1
            cnt += 1
        else:
            N -= 1
            cnt += 1
print(cnt)
