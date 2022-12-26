import sys

sys.stdin = open("1107.txt", "r")

N = int(input())
a = int(input())
if a != 0:
    breakdown = set(map(int, input().split()))
else:
    breakdown = set()
button = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
able_button = list(button ^ breakdown)

remote_control_list = []
check = False
for i in list(str(N)):
    i = int(i)
    cha = 10
    if remote_control_list:
        if remote_control_list[-1] < int(list(str(N))[len(remote_control_list) - 1]):
            check = True
    remote_control_list.append(10)
    for j in able_button:
        if check == False:
            if cha >= abs(i - j):
                cha = abs(i - j)
                remote_control_list[-1] = j
        else:
            remote_control_list[-1] = max(able_button)

# print(remote_control_list)
remote_control = ""
for i in remote_control_list:
    remote_control += str(i)
remote_control = int(remote_control)
# print(remote_control)

if (abs(N - remote_control) + len(remote_control_list)) >= abs(N - 100):
    print(abs(N - 100))
else:
    print(abs(N - remote_control) + len(remote_control_list))
