import sys
sys.stdin = open("1986.txt", "r")
T = int(input())
t = 0
for test_case in range(1, T + 1):
    N = int(input())
    t += 1
    answer = 0
    for i in range(1, N+1):
        if i % 2 == 1:
            answer += i
        else: 
            answer -= i
    print(f"#{t}",answer)
