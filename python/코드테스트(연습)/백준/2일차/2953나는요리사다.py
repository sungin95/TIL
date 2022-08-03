a = map(int, input().split())
b = map(int, input().split())
c = map(int, input().split())
d = map(int, input().split())
e = map(int, input().split())

dict_ = {}
list_ = []
cnt = 0

for i in [a,b,c,d,e]:
    i_sum = (sum(i))
    cnt += 1
    list_.append(i_sum)
    dict_[f"{cnt}"] = i_sum
for i in dict_:
    if max(list_) == dict_[f"{i}"]:
        print(f"{i} {max(list_)}")
        break
# sum 이란건 계산 후에는 해당 식을 비워버리네?