T = int(input())
for t in range(T):
    answer = 1
    puzzle_list = []
    for i in range(9):
        data = input().split()
        puzzle_list.append(data)
        if len(set(data)) != 9:
            answer = 0
    for i in range(9):
        if answer == 1:
            check = set()
            for j in range(9):
                check.add(puzzle_list[j][i])
            else:
                if len(check) != 9:
                    answer = 0
        else:
            break
        
        a = 0
        b = 0
        for _ in range(9):
            check = set()
            if answer == 1:
                for i in range(a, 3+a):
                    for j in range(b,3+b):
                        check.add(puzzle_list[i][j])
                else:
                    if len(check) != 9:
                        answer = 0
                    a += 3
                    if a == 9:
                        a = 0
                        b += 3
            else: 
                break
    print(f"#{t+1} {answer}")

