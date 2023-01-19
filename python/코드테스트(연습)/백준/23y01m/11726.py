N = int(input())

fibo = [1, 1]

for i in range(1, N):
    new = fibo[i - 1] + fibo[i]
    fibo.append(new)

print(fibo[-1] % 10007)
