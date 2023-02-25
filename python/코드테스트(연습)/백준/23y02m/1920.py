N = input()
N_list = list(map(int, input().split()))
M = input()
M_list = list(map(int, input().split()))

N_dict = {}
for i in N_list:
    N_dict[i] = 1

for i in M_list:
    if N_dict.get(i) == None:
        print(0)
    else:
        print(1)
