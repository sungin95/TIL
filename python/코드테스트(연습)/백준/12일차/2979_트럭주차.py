import sys

sys.stdin = open("2979.txt","r")

A,B,C = map(int, input().split())
start = []
end = []
total = []
stack = []
for _ in range(3):
    a, b = map(int, input().split())
    start.append(a)
    end.append(b)
    total.append(a)
    total.append(b)
difference = total[0]
before = total[0]
total.sort()
answer = 0
abc = 0
for current in total:
    difference = current-before
    before = current
    if len(stack) == 1:
        abc = A
    elif len(stack) == 2:
        abc = B*2
    elif len(stack) == 3:
        abc = C*3
    else:
        abc = 0
    answer += difference * abc 
    if current in start:
        stack.append("O")
    if current in end:
        stack.pop()
print(answer)


