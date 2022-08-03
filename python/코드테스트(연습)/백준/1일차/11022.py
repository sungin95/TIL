a = int(input())
for i in range(1, a+1):
    b, c = map(int, input().split())
    print(f"Case #{i}: {b} + {c} = {b + c}")