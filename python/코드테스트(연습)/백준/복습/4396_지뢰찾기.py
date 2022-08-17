from pprint import pprint
import sys
sys.stdin = open("4396.txt","r")
N = int(input())
mine_dict = {}
dy = [ 1,1,1, 0,0,-1,-1,-1]
dx = [-1,0,1,-1,1,-1, 0, 1]
for i in range(N):
    for j in range(N):
        mine_dict[(i,j)] = 0
for i in range(N):
    data = input()
    for j in range(N):
        if data[j] == '*':
            mine_dict[(i,j)] = "*"
            for n in range(8):
                if 0 <= i+dy[n] and i+dy[n] < N and 0 <= j+dx[n] and j+dx[n] < N and mine_dict[(i+dy[n],j+dx[n])] != "*":
                    mine_dict[(i+dy[n],j+dx[n])] += 1
answer_list = []
check = False
for i in range(N):
    data = input()
    answer = []
    for j in range(N):
        if data[j] == "x":
            if mine_dict[(i,j)] == None:
                answer.append("0")
            elif mine_dict[(i,j)] == "*":
                answer.append("0")
                check = True
            else:
                answer.append(str(mine_dict[(i,j)]))
        else:
            answer.append(".")
    else:
        answer_list.append(answer)
if check == True:
    for ij in mine_dict:
        if mine_dict[ij] == "*":
            answer_list[ij[0]][ij[1]] = "*"
for ans in answer_list:
    for an in ans:
        print(an,end="")
    else:
        print()
