board = []
board_dict = {}
for _ in range(19):
    data = list(map(int, input().split()))
    board.append(data)
check = False
for i in range(19):
    for j in range(19):
        board_dict[(i,j)] = board[i][j]

for j in range(19):
    if check == False:
        for i in range(19):
            if board_dict[(i,j)] == 1:
                if j + 4 <= 18:
                    if board_dict[(i,j+1)] == 1 and board_dict[(i,j+2)] == 1 and board_dict[(i,j+3)] == 1 and board_dict[(i,j+4)] == 1 and board_dict.get((i,j+5)) != 1 and board_dict.get((i,j-1)) != 1:
                        print(1)
                        print(i+1,j+1)
                        check = True
                        break
                    if i + 4 <= 18:
                        if board_dict[(i+1,j+1)] == 1 and board_dict[(i+2,j+2)] == 1 and board_dict[(i+3,j+3)] == 1 and board_dict[(i+4,j+4)] == 1 and board_dict.get((i+5,j+5)) != 1 and board_dict.get((i-1,j-1)) != 1:
                            print(1)
                            print(i+1,j+1)
                            check = True
                            break
                    if i - 4 >= 0:
                        if board_dict[(i-1,j+1)] == 1 and board_dict[(i-2,j+2)] == 1 and board_dict[(i-3,j+3)] == 1 and board_dict[(i-4,j+4)] == 1 and board_dict.get((i-5,j+5)) != 1 and board_dict.get((i+1,j-1)) != 1:
                            print(1)
                            print(i+1,j+1)
                            check = True
                            break
                if i + 4 <= 18:
                    if board_dict[(i+1,j)] == 1 and board_dict[(i+2,j)] == 1 and board_dict[(i+3,j)] == 1 and board_dict[(i+4,j)] == 1 and board_dict.get((i+5,j)) != 1 and board_dict.get((i-1,j)) != 1:
                        print(1)
                        print(i+1,j+1)
                        check = True
                        break
            

            elif board_dict[(i,j)] == 2:
                if j + 4 <= 18:
                    if board_dict[(i,j+1)] == 2 and board_dict[(i,j+2)] == 2 and board_dict[(i,j+3)] == 2 and board_dict[(i,j+4)] == 2 and board_dict.get((i,j+5)) != 2 and board_dict.get((i,j-1)) != 2:
                        print(2)
                        print(i+1,j+1)
                        check = True
                        break
                    if i + 4 <= 18:
                        if board_dict[(i+1,j+1)] == 2 and board_dict[(i+2,j+2)] == 2 and board_dict[(i+3,j+3)] == 2 and board_dict[(i+4,j+4)] == 2 and board_dict.get((i+5,j+5)) != 2 and board_dict.get((i-1,j-1)) != 2:
                            print(2)
                            print(i+1,j+1)
                            check = True
                            break
                    if i - 4 >= 0:
                        if board_dict[(i-1,j+1)] == 2 and board_dict[(i-2,j+2)] == 2 and board_dict[(i-3,j+3)] == 2 and board_dict[(i-4,j+4)] == 2 and board_dict.get((i-5,j+5)) != 2 and board_dict.get((i+1,j-1)) != 2:
                            print(2)
                            print(i+1,j+1)
                            check = True
                            break
                if i + 4 <= 18:
                    if board_dict[(i+1,j)] == 2 and board_dict[(i+2,j)] == 2 and board_dict[(i+3,j)] == 2 and board_dict[(i+4,j)] == 2 and board_dict.get((i+5,j)) != 2 and board_dict.get((i-1,j)) != 2:
                        print(2)
                        print(i+1,j+1)
                        check = True
                        break
                    

if check == False:
    print(0)
                
                


            