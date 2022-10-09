n, m = map(int, input().split())

arr = sorted(list(map(int, input().split())))

answer_list = []

def bfs():
    if len(answer_list) == m:
        print(*answer_list)
    else:
        for i in arr:
            if i not in answer_list:
                try:
                    if max(answer_list) <= i:
                        answer_list.append(i)
                        bfs()
                        answer_list.pop()
                except:
                    answer_list.append(i)
                    bfs()
                    answer_list.pop()

bfs()