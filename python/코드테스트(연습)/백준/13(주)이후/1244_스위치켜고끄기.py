import sys
sys.stdin = open("1244.txt","r")

N = int(input())

bulb = list(map(int, input().split()))
M = int(input())
for _ in range(M):
    gender, num = map(int, input().split())
    if gender == 1: 
        nn = N//num 
        k = 0
        for n in range(1,nn+1):
            if bulb[(n*num)-1] == 1:
                bulb[(n*num)-1] = 0
            else:
                bulb[(n*num)-1] = 1
    else:
        i = 0
        if bulb[num -1] == 1:
            bulb[num -1] = 0
        else:
            bulb[num -1] = 1
        while True:
            i += 1
            if 0 <= num-1-i and num-1+i < N and bulb[num-1+i] == bulb[num-1-i]:
                for j in [i,-i]:
                    if bulb[num -1+ j] == 1:
                        bulb[num -1+ j] = 0
                    else:
                        bulb[num -1 + j] = 1
            else:
                break
cnt = 10
for ans in bulb:
    if cnt % 30 == 0:
        print()
        cnt = 10
    cnt += 1
    print(ans,end=" ")