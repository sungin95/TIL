import sys
sys.stdin = open("2579.txt", "r")

from copy import copy
stair = []
answer = 0
t = int(input())
for i in range(t):
    data = int(input())
    stair.append(data)
answer_list = []
answer_list.append(0)
answer = 0
stair2 = []
stair2.append(stair[:])
cnt = 0
len_ans = [len(stair)]

for st in stair2:
    if st == []:
        continue
    answer = answer_list[cnt]
    cnt += 1
    step_1 = st.pop()
    answer += step_1
    answer_list.append(answer)
    if st == []:
        len_ans.append(0)
        stair2.append([])
        continue

    step_2 = st.pop()
    sta = copy(st)

    if len(sta) not in len_ans:
        len_ans.append(len(sta))
        stair2.append(sta)
    else:
        index_a = len_ans.index(len(sta))
        if answer_list[index_a] < answer:
            answer_list[index_a] = answer
        answer_list.pop()

    answer += step_2
    answer_list.append(answer)
    if st == []:
        len_ans.append(0)
        stair2.append([])
        continue
    st.pop()
    stb = copy(st)

    if len(stb) not in len_ans:
        len_ans.append(len(stb))
        stair2.append(stb)
    else:
        index_b = len_ans.index(len(stb))
        if answer_list[index_b] < answer:
            answer_list[index_b] = answer
        answer_list.pop()

print(max(answer_list))





