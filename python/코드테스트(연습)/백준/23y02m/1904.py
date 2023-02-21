N = int(input())

fibo = [1, 2]
if N == 1:
    print(1)
elif N == 2:
    print(2)
else:
    for i in range(2, N):
        fi = (fibo[i - 1] + fibo[i - 2]) % 15746
        fibo.append(fi)
    print(fibo[-1])
