n, m = map(int, input().split())

arr = []

answer_list = []


def dfs():
    if len(arr) == m:
        print(*arr)
        return
    else:
        for i in range(1, n+1):
            arr.append(i)
            dfs()
            arr.pop()


dfs()
