N, M = map(int, input().split())
parking_space = []
parking = [[],[],[],[],[]]
ny = [0,0,1,1]
nx = [0,1,0,1]
for _ in range(N):
    data = list(input())
    parking_space.append(data)
for y in range(N-1):
    for x in range(M-1):
        if parking_space[y][x] != "#":
            cnt = 0
            for k in range(4):
                if parking_space[y+ny[k]][x+nx[k]] == "X":
                    cnt += 1
                elif parking_space[y+ny[k]][x+nx[k]] == "#":
                    break
            else:
                parking[cnt].append("O") 
for ans in range(5):
    print(len(parking[ans]))
            