T = int(input())
answer = []
for t in range(T):
    num = int(input())
    answer.append(num)
answer.sort()
for ans in answer:
    print(ans)