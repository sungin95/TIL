N, M = map(int,input().split())
data = sorted(list(map(int, input().split())))
max_list = []
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            sum_ = data[i]+data[j]+data[k]
            if sum_ <= M:
                max_list.append(sum_)
            else:
                break
print(max(max_list))