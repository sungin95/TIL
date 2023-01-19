import sys

sys.stdin = open("9935.txt", "r")

import sys

str_ = sys.stdin.readline().rstrip()
boom = sys.stdin.readline().rstrip()

str_2 = list()
for i in range(len(str_)):
    str_2.append(str_[i])
    if len(str_2) >= len(boom):
        if "".join(str_2[-len(boom) :]) == boom:
            for _ in range(len(boom)):
                str_2.pop()

if str_2 == []:
    print("FRULA")
else:
    print("".join(str_2))
