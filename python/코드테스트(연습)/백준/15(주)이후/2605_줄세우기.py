t = int(input())
cnt = 0
order = list(map(int, input().split()))
answer = []
for i in range(t):
    cnt += 1
    answer.insert(order[cnt-1],cnt)
answer.reverse()
print(*answer)