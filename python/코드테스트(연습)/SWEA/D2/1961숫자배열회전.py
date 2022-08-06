import sys
sys.stdin = open("1961.txt", "r")

# T = int(input())
# for t in range(T):

N = int(input()) 
arr = []
for n in range(N):
    num = list(map(str, input().split()))
    arr.append(num)
print(arr)
for n in range(N):
    for m in range(N-1,-1, -1):
        print(arr[m][n], end="")
    else:
        print(end=" ")
print()
for n in range(N): # n은 정상수
    for m in range(N-1,-1, -1): # m은 역수
        print(arr[m][n], end="")
    else:
        print(end=" ") 
# for n in range(N):
#     print(arr[2][n]+arr[1][n]+arr[0][n], end=" ")