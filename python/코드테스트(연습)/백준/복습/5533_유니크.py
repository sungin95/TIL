from pprint import pprint
import sys
sys.stdin = open("5533.txt","r")
N = int(input())
score = []
a = []
b = []
c = []
for _ in range(N):
    sc = list(map(int, input().split()))
    score.append(sc)
    a.append(sc[0])
    b.append(sc[1])
    c.append(sc[2])
answer = []
for s in score:
    sum_ = 0
    if a.count(s[0]) == 1:
        sum_ += s[0]
    if b.count(s[1]) == 1:
        sum_ += s[1]
    if c.count(s[2]) == 1:
        sum_ += s[2]
    answer.append(sum_)

for ans in answer:
    print(ans)
