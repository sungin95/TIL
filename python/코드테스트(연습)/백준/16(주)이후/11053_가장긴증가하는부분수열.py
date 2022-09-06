
import sys
sys.stdin = open("11053.txt", "r")



_ = int(input())
data = list(map(int, input().split()))



increase = 0
n = len(data)
cnt = 0
for i in range(n):
    A = data.popleft()
    if increase < A:
        increase = A
        cnt += 1
print(cnt)

