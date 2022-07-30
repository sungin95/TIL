N = int(input())
N_card = list(map(int, input().split()))
M = int(input())
M_card = list(map(int, input().split()))

N_card_dict = {}
for i in N_card:
    if N_card_dict.get(i) == None:
        N_card_dict[i] = 1
    else:
        N_card_dict[i] += 1

for j in M_card:
    if N_card_dict.get(j) == None:
        print(0, end=" ")
    else:
        print(N_card_dict[j], end=" ")
