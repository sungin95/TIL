N = int(input())
members = []
for i in range(N):
    a1, a2 = input().split()
    a1 = int(a1)
    members.append([a1, a2])
members.sort(key=lambda x: x[0])
for m in members:
    print(m[0], m[1])
