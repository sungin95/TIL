import sys

n = int(sys.stdin.readline())

S = set()

for _ in range(n):
    c = sys.stdin.readline().strip().split()
    if len(c) == 1:
        if c[0] == "all":
            S = set([i for i in range(1, 21)])
        elif c[0] == "empty":
            S = set()
    if len(c) == 2:
        c[1] = int(c[1])
        if c[0] == "check":
            if c[1] in S:
                print(1)
            else:
                print(0)
        elif c[0] == "add":
            S.add(c[1])
        elif c[0] == "remove":
            try:
                S.remove(c[1])
            except:
                pass
        elif c[0] == "toggle":
            if c[1] in S:
                S.remove(c[1])
            else:
                S.add(c[1])
