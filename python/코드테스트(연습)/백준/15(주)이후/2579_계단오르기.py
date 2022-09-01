import sys
sys.stdin = open("2579.txt", "r")

t = int(input())
stair_list = []
max_answer = 0
i_list = []
for i in range(t):
    stair = int(input())
    stair_list.append(stair)
    i_list.append(i)
i = 0
jump_cnt = 0
if t == 3:
    max_answer = sum(stair_list) - min(stair_list)
    print(max_answer)
else:
    while i != t:
        print(i)
        print(i_list)
        jump_list = []
        jump_stair = 0
        for j in range(1,4):
            if i+j < t:
                jump_list.append(stair_list[i+j])
        if len(jump_list) == 3:
            jump_stair = jump_list.index(min(jump_list))
            i += jump_stair+1
            i_list.pop(i -jump_cnt)
            jump_cnt += 1
        else: 
            break
    for i in i_list:
        max_answer += stair_list[i]
    
    print(max_answer)