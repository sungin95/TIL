N = int(input())

fibo = [0, 1]

if N == 0:
    print(0)

elif N == 1:
    print(1)
else:
    for i in range(1, N):
        a = fibo[i - 1] + fibo[i]
        fibo.append(a)
    print(fibo[-1])
