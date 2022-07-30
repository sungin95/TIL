N, M = map(int, input().split())
names = []
for i in range(N+M):
    names += input().split()




names_dict = {}
answer = []
for i in names:
    if names_dict.get(i) == None:
        names_dict[i] = 1
    else:
        names_dict[i] += 1

for j in names_dict:
    if names_dict[j] == 2:
        answer.append(j)
answer.sort()
print(len(answer))
for k in answer:
    print(k)

