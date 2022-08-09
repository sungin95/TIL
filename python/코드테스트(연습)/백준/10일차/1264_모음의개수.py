answer_list = []
while True:
    str_ = input()
    str_line =str_.lower()

    if str_line == "#":
        break
    a = str_line.count("a")
    e = str_line.count("e")
    i = str_line.count("i")
    u = str_line.count("u")
    o = str_line.count("o")
    answer = a+e+i+u+o
    answer_list.append(answer)
for ans in answer_list:
    print(ans)