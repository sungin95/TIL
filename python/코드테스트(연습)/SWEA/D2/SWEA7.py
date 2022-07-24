N = int(input())

answer = 0
for i in range(1, N+1):
    if i % 2 == 1:
        answer += i
    else: 
        answer -= i
print(answer)
