N, X = map(int, input().split())
A = map(int, input().split())
for num in A:
    if num < X:
        print(num, end=" ")