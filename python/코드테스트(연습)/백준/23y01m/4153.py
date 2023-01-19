answer_list = []
while True:
    A, B, C = map(int, input().split())
    if (A, B, C) == (0, 0, 0):
        break
    AAA = [A, B, C]
    AAA.sort()
    if AAA[2] ** 2 == AAA[0] ** 2 + AAA[1] ** 2:
        answer_list.append("right")
    else:
        answer_list.append("wrong")

for answer in answer_list:
    print(answer)
