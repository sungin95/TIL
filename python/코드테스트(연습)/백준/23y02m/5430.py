import sys

sys.stdin = open("5430.txt", "r")

from collections import deque

answer_list = []
T = int(input())
for t in range(T):
    P = list(input())
    n = int(input())
    n_l = input()
    n_l = n_l[1:-1]
    n_list = map(int, (n_l.replace(",", " ")).split())
    n_deque = deque(n_list)
    # false popleft, True pop
    RD = False
    try:
        for p in P:
            if p == "R":
                if RD == False:
                    RD = True
                else:
                    RD = False
            elif p == "D":
                if RD == False:
                    n_deque.popleft()
                else:
                    n_deque.pop()
        else:
            if RD == True:
                n_deque.reverse()
                answer_list.append(list(n_deque))
            else:
                answer_list.append(list(n_deque))
    except:
        answer_list.append("error")
for ans in answer_list:
    if ans == "error":
        print(ans)
    else:
        # 이게 필수!!!
        if ans == []:
            print(ans)
        else:
            answer = "["
            for a in ans:
                answer += str(a)
                answer += ","
            answer = answer[:-1]
            answer += "]"
            print(answer)
