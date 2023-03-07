import sys

sys.stdin = open("1991.txt", "r")

N = int(input())
tree = {}


for _ in range(N):
    par, son1, son2 = input().split()
    tree[par] = (son1, son2)


answer_list = []


#  전위 순회
def top_r(ans_str, start):
    ans_str[0] += start

    if tree[start][0] != ".":
        top_r(ans_str, tree[start][0])

    if tree[start][1] != ".":
        top_r(ans_str, tree[start][1])


ans_str = [""]
top_r(ans_str, "A")
answer_list.append(ans_str)


#  전위 순회
def top_r(ans_str, start):
    if tree[start][0] != ".":
        top_r(ans_str, tree[start][0])
    ans_str[0] += start

    if tree[start][1] != ".":
        top_r(ans_str, tree[start][1])


ans_str = [""]
top_r(ans_str, "A")
answer_list.append(ans_str)


#  전위 순회
def top_r(ans_str, start):
    if tree[start][0] != ".":
        top_r(ans_str, tree[start][0])

    if tree[start][1] != ".":
        top_r(ans_str, tree[start][1])
    ans_str[0] += start


ans_str = [""]
top_r(ans_str, "A")
answer_list.append(ans_str)


for a in answer_list:
    print(a[0])
