# 이 문제가 어려웠던 이유는 이전 식 2개의 값을 합해야 하는데. 
# 이때 해당 리스트가 없으면 오류가 나는데. 이걸 처리하는게 상당히 어려웠다. 
# 그래서 이 문제를 해결하기 위해 딕셔너리를 추가하였다. 
# if dict.get() == None: 을 활용하면 오류 없이 문제를 해결 할 수 있었다. 
# 그래서 정답용 리스트 하나
# 체크용 딕셔너리 하나를 만들어 주었습니다. 

N = int(input())    
for n in range(1, N+1):
    T = int(input()) 
    pascal_list = [[1]] # T가 1일때가 어려워서 다행히 T값이 1이상이라서 1일때 값을 미리 주었습니다. 
    pascal_dict = {(0,0):1}
    for t in range(1,T): # T 가 2일때부터 출력
        pascal_list.append([1])  # 줄이 바뀔때 마다 맨앞 1 추가 
        pascal_dict[(t,0)] = 0 # 모든 값은 딕셔너리에도 추가 된다. 
        for i in range(1, t+1):
            if pascal_dict.get((t-1,i)) == None: # 마지막에 1추가 
                pascal_list[t].append(1) # ! 
                pascal_dict[(t,i)] = 0
            else: # 위 두개를 더해서 값을 추가한다. 
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