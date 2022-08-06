import sys
sys.stdin = open("2167.txt", "r")

N,M = map(int,input().split())
arr = [] # 행열저장 
for i in range(N):
    data = list(map(int, input().split()))
    arr.append(data)
k = int(input())
answer = []
for i in range(k):
    i,j,x,y = map(int,input().split()) #(i,j)부터 (x,y)까지
    ans = 0 
    for i_ in range(i-1,x):
        for j_ in range(j-1,y):
            ans += (arr[i_][j_])
    answer.append(ans)
for _ in answer:
    print(_)
