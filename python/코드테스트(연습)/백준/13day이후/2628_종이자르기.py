# 이차원이 아니라 숫자로 푼 이유
# 1. 이차원으로 너무 복잡해 진다. 
# 2. 결국 자른다의 본질은 길이가 달라진다였고
# 답은 그들의 곱이었다.  

M, N = map(int, input().split())
_ = int(input())
M_list = [0,M]
N_list = [0,N]
for __ in range(_):
    a,b = map(int, input().split())
    if a == 0:
        N_list.append(b)
    else:
        M_list.append(b)
N_list.sort()
M_list.sort()
answer_N = []
answer_M = []
for i in range(1,len(N_list)):
    answer_N.append(N_list[i] - N_list[i-1])
for i in range(1,len(M_list)):
    answer_M.append(M_list[i] - M_list[i-1])
answer = []
for i in answer_N:
    for j in answer_M:
        answer.append(i*j)
print(max(answer))

