t = int(input())
area = set()
for _ in range(t):
    a,b = map(int, input().split())
    for i in range(a,a+10):
        for j in range(b, b+10):
            area.add((i,j))
print(len(area))
