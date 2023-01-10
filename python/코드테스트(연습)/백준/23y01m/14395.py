s, t = map(int, input().split())

calculation = ["+", "*"]

min_list = []
min_ = [10000000001]


def calculation_f(s, t, order):
    if min_[0] < len(order):
        return
    # print(min_list)

    if s >= t:
        if s == t:
            min_list.append(order)
            if min_[0] > len(order):
                min_[0] = len(order)
        return
    for calc in calculation:
        if calc == "*":
            s1 = s * s
        elif calc == "+":
            s1 = s + s
        order += calc
        if s1 != 1:
            # print(s1, s, t, order)
            calculation_f(s1, t, order)
            order = order[:-1]


if s == t:
    print(0)
else:
    calculation_f(s, t, "")
    calculation_f(1, t, "/")
    if min_list == []:
        print(-1)
    else:
        # 순서
        answer_list = []
        for i in range(len(min_list)):
            if len(min_list[-(i + 1)]) == min_[0]:
                a = min_list[-(i + 1)]
                answer_list.append(a)
        answer_list2 = []
        for i in answer_list:
            answer_list2.append([])
            for j in i:
                jj = ord(j)
                answer_list2[-1].append(jj)
        answer_list2.sort()
        answer = ""
        for j in answer_list2[0]:
            jj = chr(j)
            answer += jj
        print(answer)
