import sys

sys.stdin = open("11404.txt", "r")

N = int(input())
M = int(input())
# 최대값으로 제대로 해 준다.
inf = 100000000
bus_cost = [[inf for i in range(N)] for i in range(N)]

# 같은 경로가 나올때가 있어서 min은 사용해 준다.
for _ in range(M):
    a, b, cost = map(int, input().split())
    bus_cost[a - 1][b - 1] = min(cost, bus_cost[a - 1][b - 1])

# k 가 돌면서 최소값을 찾는다.
for k in range(N):
    for j in range(N):
        for i in range(N):
            # 초기 값이 0이 아닌 최대값이고 본인자리를 왔다갔다하면 0을 해 주어야 하니까.
            if i == j:
                bus_cost[j][i] = 0
            else:
                bus_cost[j][i] = min(bus_cost[j][i], bus_cost[j][k] + bus_cost[k][i])
for a in bus_cost:
    for aa in a:
        if aa == inf:
            print(0, end=" ")
        else:
            print(aa, end=" ")
    print()
