import sys

sys.stdin = open("1991.txt", "r")

N = int(input())
tree = [[] for i in range(N)]

ABC = {}
for i in range(65, 91):
    ABC[chr(i)] = i - 65

for _ in range(N):
    par, son1, son2 = input().split()
    tree[ABC[par]].append(son1)
    tree[ABC[par]].append(son2)

answer_list = []


#  전위 순회
def top_r(ans_str, start):
    for i in range(2):
        if tree[start][i] == ".":
            pass
        else:
            ans_str[0] += tree[start][i]
            top_r(ans_str, ABC[tree[start][i]])


ans_str = ["A"]
top_r(ans_str, 0)
answer_list.append(ans_str)


# 중위 순회
def top_m(ans_str, start):
    for i in range(2):
        if tree[start][i] == ".":
            pass
        else:
            if i == 0:
                ans_str[-1] = tree[start][i] + ans_str[-1]
                top_m(ans_str, ABC[tree[start][i]])
            elif i == 1:
                ans_str.append("")
                ans_str[-1] = tree[start][i] + ans_str[-1]
                top_m(ans_str, ABC[tree[start][i]])


ans_str = ["A"]
top_m(ans_str, 0)
answer = ""
for a in ans_str:
    answer += a

answer_list.append([answer])


# 하위 순회
def top_b(ans_str, ans_str2, start):
    for i in range(2):
        if tree[start][i] == ".":
            pass
        else:
            if i == 0:
                ans_str[-1] = tree[start][i] + ans_str[-1]
                top_b(ans_str, ans_str2, ABC[tree[start][i]])
            elif i == 1:
                ans_str.append("")
                ans_str2[-1] = tree[start][i] + ans_str2[-1]
                top_b(ans_str, ans_str2, ABC[tree[start][i]])


ans_str = [""]
ans_str2 = ["A"]
top_b(ans_str, ans_str2, 0)
answer = ""
for a in ans_str:
    answer += a
answer += ans_str2[0]

answer_list.append([answer])

for a in answer_list:
    print(a[0])
