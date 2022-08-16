from pprint import pprint
from collections import deque


M, n = map(int, input().split())
queue = deque([(0,1),(1,0),(0,-1),(-1,0)])
current = queue.popleft()
location = [0,0]
check = True
for _ in range(n):
    command, num = input().split()
    if command == "TURN":
        if num == "0":
            next = queue.popleft()
            queue.append(current)
            current = next
        else:
            next = queue.pop()
            queue.appendleft(current)
            current = next
    else:
        location[1]  += current[1]*int(num)
        location[0]  += current[0]*int(num)
        if not 0 <= location[0] and location[0] <= M and 0 <= location[1] and location[1] <= M:
            check = False
if check == True:
    print(f"{location[1]} {location[0]}")
else:
    print(-1)