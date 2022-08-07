from pprint import pprint
import sys
sys.stdin = open("1961.txt", "r")

T = int(input())
for t in range(T):
    N = int(input()) # N x N 행렬이다. 
    arr = [] 
    for n in range(N):
        num = list(input().split())
        arr.append(num) # 행렬 완성
        
    print(f"#{t+1}")
    a = 0 # 왼쪽에서 90도 정렬한값, 180도 정렬한값, 오른쪽에서 90도 정렬한값을 
    # 각각 제일 왼쪽에 가운데에 오른쪽에 나타내야 하는데. 
    # 90도 움직인 값을 한줄에 정렬하는 것이 아니라 각 줄을 바꾸어서 나타내야 했기 때문에
    # a의 값을 1씩 증가시켜 문제를 해결하였습니다.  
    for _ in range(N):
        a += 1
        for j in range(N-1,-1,-1): # 왼쪽 90도
            print(arr[j][a-1], end="")
        else:
            print(end=" ")
        for j in range(N-1,-1,-1): # 180도
            print(arr[N-a][j], end="")
        else:
            print(end=" ")
        for j in range(N): # 오른쪽 90도
            print(arr[j][N-a], end="")
        else:
            print(end=" ")
        print()