import sys
sys.stdin = open("2477.txt")
N = int(input())
x = 0
y = 0

a_list = []
aa_list = []
x_list = []
y_list = []
check = False
for _ in range(6):
    a,b = map(int, input().split())
    a_list.append(a)
    if a_list.count(a) == 2:
        aa_list.append(a)
    if a == 1:
        x += b
        x_list.append(x)
    elif a == 2:
        x -= b
        x_list.append(x)
    elif a == 3:
        y -= b
        y_list.append(y)
    elif a == 4:
        y += b
        y_list.append(y)

x_list.sort()
y_list.sort()
aa_list.sort()
# print(aa_list)
M_MAX = abs(y_list[2] - y_list[0]) * abs(x_list[2] - x_list[0])
if aa_list == [2,4]:
    middle = abs(y_list[2] - y_list[1]) * abs(x_list[2] - x_list[1])
    # print(1)

if aa_list == [2,3]:
    middle = abs(y_list[2] - y_list[1]) * abs(x_list[0] - x_list[1])
    # print(2)

if aa_list == [1,4]:
    middle = abs(y_list[0] - y_list[1]) * abs(x_list[2] - x_list[1])
    # print(3)

if aa_list == [1,3]:
    middle = abs(y_list[0] - y_list[1]) * abs(x_list[0] - x_list[1])
#     print(4)
# print(M_MAX,middle)
print(N*(M_MAX-middle))











# 1
# 4 10
# 2 100
# 3 100
# 1 10
# 4 90
# 1 90

# 1
# 4 10
# 2 90
# 4 90
# 2 10
# 3 100
# 1 100
