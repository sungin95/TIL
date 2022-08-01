T = int(input())
list_ = []
for i in range(T):
    a = int(input())
    if a != 0:
        list_.append(a)
    else: 
        list_.pop()
print(sum(list_))