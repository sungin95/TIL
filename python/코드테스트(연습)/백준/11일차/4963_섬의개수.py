answer_list = []

while True:  
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    island_map = []
    for _ in range(M):
        data = input().split()
        island_map.append(data)
    nx = [-1,-1,-1, 0, 0, 1,1,1]
    ny = [-1, 0, 1,-1, 1,-1,0,1]
    cnt = 0
    for y in range(M):
        for x in range(N):
            if island_map[y][x] == "1":
                island_map[y][x] = "0"
                island_list = []
                island_list.append([y,x])
                y_same = y
                x_same = x
                while True:
                    for n in range(8):
                        if 0 <= y_same+ny[n] and y_same+ny[n] < M and 0 <= x_same+nx[n] and x_same+nx[n] < N:
                            if island_map[y_same+ny[n]][x_same+nx[n]] == "1":
                                island_list.append([y_same+ny[n],x_same+nx[n]])
                                island_map[y_same+ny[n]][x_same+nx[n]] = "0"
                    else:
                        try:
                            a = island_list.pop()
                            y_same = a[0]
                            x_same = a[1]
                        except:
                            cnt += 1
                            break
    answer_list.append(cnt)
for ans in answer_list:
    print(ans)

