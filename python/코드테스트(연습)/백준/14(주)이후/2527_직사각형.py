import sys
sys.stdin = open("2527.txt","r")

input = sys.stdin.readline

answer_list = []
for _ in range(4):
    a,b,c,d,e,f,g,h = map(int,input().split())
    ac_set = set()
    bd_set = set()
    eg_set = set()
    fh_set = set()
    for i in range(a,c+1):
        ac_set.add(i)
    for i in range(b,d+1):
        bd_set.add(i)
    for i in range(e,g+1):
        eg_set.add(i)
    for i in range(f,h+1):
        fh_set.add(i)
    len_x = (len(ac_set & eg_set))
    len_y = (len(bd_set & fh_set))
    if len_x == 0 or len_y == 0:
        answer_list.append("d")
    elif len_x == 1 and len_y == 1:
        answer_list.append("c")
    elif (len_x >= 2 or len_y >= 2) and (len_x == 1 or len_y == 1):
        answer_list.append("b")
    elif len_x >= 2 and len_y >= 2:
        answer_list.append("a")
for ans in answer_list:
    print(ans)