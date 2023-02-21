N = int(input())
sanggn = list(map(int, input().split()))
card_dict = {}
for sang in sanggn:
    card_dict[sang] = 1
answer_list = []
M = map(int, input().split())
YN = list(map(int, input().split()))
for yn in YN:
    if card_dict.get(yn) == None:
        answer_list.append(0)
    else:
        answer_list.append(1)
print(*answer_list)
