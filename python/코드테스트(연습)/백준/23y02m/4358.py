import sys

sys.stdin = open("4358.txt", "r")


tree_dict = {}
cnt = 0
for line in sys.stdin:
    if line == "\n":
        break

    tree = line.rstrip()

    cnt += 1
    if tree_dict.get(tree) == None:
        tree_dict[tree] = 1
    else:
        tree_dict[tree] += 1


tree_list = []
for k in tree_dict.keys():
    tree_list.append(k)
tree_list.sort()

for t in tree_list:
    percentage = round((tree_dict[t] / cnt) * 100, 4)
    print(t, "%.4f" % percentage)
