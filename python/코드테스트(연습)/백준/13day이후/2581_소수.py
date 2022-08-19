import sys
sys.stdin = open("2581.txt","r")

MIN_N = int(input())
MAX_N = int(input())
prime_number = []
num_list = [0,0] # 0과 1은 소수가 아니라서 미리 넣어줬습니다. 
for i in range(2,MAX_N+1): # 2부터 끝 위치인덱스가 MAX_N랑 같을때 까지 1추가.
    num_list.append(1)

for j in range(MAX_N+1):# 
    i = 2
    if num_list[j] == 1:
        while (j*i) < MAX_N+1:
            num_list[j*i] = 0
            i += 1

for j in range(MIN_N,MAX_N+1): # 최소값 이상 소수를 prime_number에 append
    if num_list[j] == 1:
        prime_number.append(j)

if prime_number == []:
    print(-1)
else:
    print(sum(prime_number))
    print(min(prime_number))



