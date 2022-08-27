import sys
sys.stdin = open("1244.txt","r")

N = int(input())

bulb = list(map(int, input().split()))
M = int(input())
for _ in range(M):
    gender, num = map(int, input().split())
    if gender == 1: # 남자일때 
        nn = N//num 
        k = 0
        for n in range(1,nn+1):
            if bulb[(n*num)-1] == 1:
                bulb[(n*num)-1] = 0
            else:
                bulb[(n*num)-1] = 1
    else: # 여자일때 
        i = 0
        if bulb[num -1] == 1: # 맨 처음 
            bulb[num -1] = 0
        else:
            bulb[num -1] = 1
        while True:
            i += 1
            if 0 <= num-1-i and num-1+i < N and bulb[num-1+i] == bulb[num-1-i]: # 조건에 맞는지 체크 
                for j in [i,-i]: # 각각 바꾼다. 
                    if bulb[num -1+ j] == 1:
                        bulb[num -1+ j] = 0
                    else:
                        bulb[num -1 + j] = 1
            else:
                break
cnt = 0
for ans in bulb:
    cnt += 1
    print(ans,end=" ")
    if cnt % 20 == 0:
        print()
        cnt = 0