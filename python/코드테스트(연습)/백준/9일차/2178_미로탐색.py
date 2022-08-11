maze_list = []
N, M = map(int, input().split())
for n in range(N):
    data = input()
    maze_list.append([])
    for char in data:
        maze_list[n].append(int(char))

cnt = 1
maze_list[0][0] = 2
while maze_list[N-1][M-1] == 1:
    cnt += 1
    for i in range(N):
        for j in range(M):
            if maze_list[i][j] == cnt:
                if i +1 < N:
                    if maze_list[i+1][j] == 1:
                        maze_list[i+1][j] = cnt+1
                if j +1 < M:
                    if maze_list[i][j+1] == 1:
                        maze_list[i][j+1] = cnt+1
                if i -1 >= 0:
                    if maze_list[i-1][j] == 1:
                        maze_list[i-1][j] = cnt+1
                if j -1 >= 0:
                    if maze_list[i][j-1] == 1:
                        maze_list[i][j-1] = cnt+1
print(maze_list[N-1][M-1]-1)
    
