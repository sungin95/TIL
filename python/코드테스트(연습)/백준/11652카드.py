T = int(input())
num_dict = {} 
max_ = 0 
frequent_integer = []
for i in range(T): # 우선 카운터를 해 준다. 
    num = input()
    if num_dict.get(num) == None:
        num_dict[num] = 1
    else:
        num_dict[num] += 1

for num in num_dict: # 이중 가장 많이 팔린 값을 알아내고 리스트를 만든다. 
    if max_ <= num_dict[num]:
        if max_ == num_dict[num]:
            frequent_integer.append(int(num))
        
        else:
            frequent_integer.clear()
            max_ = num_dict[num]
            frequent_integer.append(int(num))
        

answer = min(frequent_integer) # 최소값이 답

print(answer)
# if int(answer[0]) < 0: 식이 오래 걸려서 min식으로 바꿈. 
#     for i in range(len(answer)):
#         if int(answer[i]) >= 0:
#             print(answer[i-1])
#             break
# else:
#     print(int(answer[0]))
