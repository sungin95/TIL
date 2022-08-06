import sys
from pprint import pprint
sys.stdin = open("5533.txt", "r")
N = int(input())

abc_list = []

for i in range(N):
    abc = list(map(int, input().split()))
    abc_list.append(abc)

pprint(abc_list)
back = []
for x in range(3):
    col = []
    for y in range(5):
        col.append(abc_list[y][x])
    back.append(col)
pprint(back)
    
score_list = [0] * 5
for x in range(3): # ! 이 부분을 잘 안되는 부분이다. 
    col = back[x]
    for y in range(5):
        score = col[y]
        if col.count(score) == 1:
            score_list[y] += score
print(score_list)

        
    


