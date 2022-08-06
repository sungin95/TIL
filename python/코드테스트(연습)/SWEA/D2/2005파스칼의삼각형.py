N = int(input())    
for n in range(1, N+1):
    T = int(input())
    pascal_list = [[1]]
    pascal_dict = {(0,0):1}
    for t in range(1,T): # t == 1
        i = 0
        pascal_list.append([1])  # ! 
        pascal_dict[(t,i)] = 0
        for i in range(t):
            i += 1
            if pascal_dict.get((t-1,i)) == None:
                pascal_list[t].append(1) # ! 
                pascal_dict[(t,i)] = 0
            else: 
                a = pascal_list[t-1][i-1] + pascal_list[t-1][i]
                pascal_list[t].append(a) # ! 
                pascal_dict[(t,i)] = 0
    print(f"#{n}")
    for ans in pascal_list:
        print(*ans)


# T = 5
# pascal_list = [[1]]
# pascal_dict = {(0,0):1}
# for t in range(1,T): # t == 1
#     i = 0
#     pascal_list.append([1])  # ! 
#     pascal_dict[(t,i)] = 0
#     for i in range(t):
#         print(pascal_list)
#         print(pascal_dict)
#         i += 1
#         if pascal_dict.get((t-1,i)) == None:
#             pascal_list[t].append(1) # ! 
#             pascal_dict[(t,i)] = 0
#             print(pascal_list)
#             print(pascal_dict)
#         else: 
#             a = pascal_list[t-1][i-1] + pascal_list[t-1][i]
#             pascal_list[t].append(a) # ! 
#             pascal_dict[(t,i)] = 0