sys.stdin = open("9935.txt", "r")
import sys

str_ = sys.stdin.readline().rstrip()
boom = sys.stdin.readline().rstrip()


def str__function(str_, boom):
    str_2 = list()
    for i in range(len(str_)):
        str_2.append(str_[i])
        # "".join(str_2[-len(boom) :]) 신기한 구조
        if "".join(str_2[-len(boom) :]) == boom:
            for _ in range(len(boom)):
                str_2.pop()
    return str_2


str_ = str__function(str_, boom)

answer = ""
for a in str_:
    answer += a
if answer == "":
    print("FRULA")
else:
    print(answer)
