num_list = []
for _ in range(5):
    data = int(input())
    num_list.append(data)
num_list.sort()
sum_ = sum(num_list)
print(sum_//5)
print(num_list[2])
