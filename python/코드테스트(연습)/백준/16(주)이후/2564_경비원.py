import sys
sys.stdin = open("2564.txt", "r")

x, y = map(int, input().split())
t = int(input())
location = []
distinct = 0
for _ in range(t):
    a,b = map(int, input().split())
    location.append([a,b])
a,b = map(int, input().split())
if a == 1:
    for lo in location:
        if lo[0] == 3:
            distinct += b
            distinct += lo[1]
        elif lo[0] == 4:
            distinct += x - b
            distinct += lo[1]
        elif lo[0] == 1:
            distinct += abs(b - lo[1])
        elif lo[0] == 2:
            distinct += y
            distinct += min(lo[1] + b , x - lo[1] + x - b)
if a == 2:
    for lo in location:
        if lo[0] == 3:
            distinct += b
            distinct += y - lo[1]
        elif lo[0] == 4:
            distinct += x - b
            distinct += y - lo[1]
        elif lo[0] == 2:
            distinct += abs(b - lo[1])
        elif lo[0] == 1:
            distinct += y
            distinct += min(lo[1] + b , x - lo[1] + x - b)
if a == 3:
    for lo in location:
        if lo[0] == 1:
            distinct += b
            distinct += lo[1]
        elif lo[0] == 2:
            distinct += y - b
            distinct += lo[1]
        elif lo[0] == 3:
            distinct += abs(b - lo[1])
        elif lo[0] == 4:
            distinct += x
            distinct += min(lo[1] + b , y - lo[1] + y - b)
if a == 4:
    for lo in location:
        if lo[0] == 1:
            distinct += b
            distinct += x - lo[1]
        elif lo[0] == 2:
            distinct += y - b
            distinct += x - lo[1]
        elif lo[0] == 4:
            distinct += abs(b - lo[1])
        elif lo[0] == 3:
            distinct += x
            distinct += min(lo[1] + b , y - lo[1] + y - b)

print(distinct)
