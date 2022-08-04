sum_ = 0
set_ = set()
kbg_dict = {}
for i in range(10):
    num = int(input())
    sum_ += num 

    set_.add(num) # 딕셔너리 키값 찾기 위해
    if kbg_dict.get(num) == None: # 딕셔너리 이용하여 카운트 
        kbg_dict[num] = 1
    else:
        kbg_dict[num] += 1

max_ = 0 # 최빈수 횟수
answer = 0 # 최빈수 값
for n in set_: # 딕셔너리 값중 최빈수 찾기 
    if kbg_dict[n] > max_:
        max_ = kbg_dict[n]
        answer = n
print(sum_//10)
print(answer)