from copy import copy
import sys
sys.stdin = open("14889.txt", 'r')

n = int(input())
arr = []
group = []
synergy = []
for i in range(n):
    data = list(map(int, input().split()))
    synergy.append(data)


def dfs():  # 팀을 짤 수 있는 모든 경우의 수
    if len(arr) == n//2:
        arr_r = copy(arr)
        group.append(arr_r)
        return
    else:
        for i in range(1, n+1):
            if arr == []:
                arr.append(i)
                dfs()
                arr.pop()
            else:
                if i >= max(arr):
                    if i not in arr:
                        arr.append(i)
                        dfs()
                        arr.pop()


dfs()
# dfs()에 의해 group 이 완성이 되었다.

team_power = 0
team_power_list = []
for g in group:
    team_power = 0
    for i in range(len(g)):  # 각 사람마다 시너지 체크
        for j in range(1, len(g)):
            team_power += synergy[g[0]-1][g[j]-1]
        A = g.pop(0)
        g.append(A)
    else:  # 마지막 합을 append해 준다.
        team_power_list.append(team_power)


answer = 0
answer_list = []
# 답은 우리팀과 반대팀의 차이다. gruop[0]와 gruop[-1]은 서로 겹치는게 없는 쌍이다.
for i in range(len(team_power_list)//2):
    answer = abs(team_power_list[i] - team_power_list[-i-1])
    answer_c = copy(answer)
    answer_list.append(answer)
print(min(answer_list))
