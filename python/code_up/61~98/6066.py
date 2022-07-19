a,b,c = map(int, input().split())

m = [a, b, c]
for i in m:
    if i % 2 == 0:
        print("even")
    elif i % 2 == 1:
        print("odd")
        