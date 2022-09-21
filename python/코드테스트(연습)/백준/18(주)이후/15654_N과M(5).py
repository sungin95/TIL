n, m = map(int, input().split())
num = sorted(list(map(int, input().split())))
arr = []


def dfs():
    if len(arr) == m:
        print(*arr)
        return
    else:
        for n in num:
            if n not in arr:
                arr.append(n)
                dfs()
                arr.pop()


dfs()
