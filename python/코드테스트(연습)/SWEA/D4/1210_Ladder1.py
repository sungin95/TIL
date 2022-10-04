import sys
sys.stdin = open("1210.txt", "r")
from collections import deque


for t in range(1,11):
    bored = deque()
    _ = input()
    for i in range(100):
        data = list(map(int, input().split()))
        bored.appendleft(data)
    start = 0
    for i in range(100):
        if bored[0][i] == 2:
            start = i
    dx = [-1,1]
    step = 0
    # start, dx. step bored[step][start]
    while True:
        if step == 99:
            print(f"#{t}",start)
            break
        check = False
        for i in range(2):
            if check == False:
                while True:
                    nx = start + dx[i]
                    if 0 <= nx and nx < 100:
                        if bored[step][nx] == 1:
                            start = nx
                            check = True
                        else:
                            break
                    else:
                        break
        else:
            step += 1



            





