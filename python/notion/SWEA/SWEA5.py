num = int(input())

t = 0
for i in range(num + 1):
    answer = 2**t
    print(answer, end=" ")
    t += 1