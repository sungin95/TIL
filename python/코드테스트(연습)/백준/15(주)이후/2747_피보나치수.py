N = int(input())
def Fibonacci_sequence(N):
    global cnt
    global answer
    cnt += 1
    answer.append(answer[1])
    answer[2] += answer[0]
    answer.pop(0)
    if cnt == N:
        return answer
    else:
        Fibonacci_sequence(N)

cnt = 0
answer = [0,1]
if N == 0:
    print(1)
else:
    Fibonacci_sequence(N)
print(answer[0])