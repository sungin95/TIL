import sys
sys.stdin = open("1984.txt", "r")
T = int(input())
for test_case in range(1, T + 1):
    N = list(map(int, input().split())) 
    N.sort()
    sum = 0
    for i in range(1,len(N)-1):
        sum += N[i]
    answer = format(sum / (len(N)-2),".1f")
    print(f'#{test_case} {answer}')

