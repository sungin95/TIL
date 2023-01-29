import sys

sys.stdin = open("1068.txt", "r")

N = int(input())
tree = list(map(int, input().split()))
remove_num = int(input())

# 트리 지우기 함수 재귀함수를 이용
def remove_node(r):
    tree[r] = -2
    for i in range(len(tree)):
        if r == tree[i]:
            tree[i] = -2
            remove_node(i)


remove_node(remove_num)
count = 0
for i in range(len(tree)):
    # 지운거랑 뻗은 가지가 없으면 카운트
    if tree[i] != -2 and i not in tree:
        count += 1

print(count)
