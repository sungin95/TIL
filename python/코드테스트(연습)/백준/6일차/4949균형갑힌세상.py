answer = []
while True:
    A = [] # () []
    str_ = input()
    if str_ == ".":
        break
    try:
        for char in str_:
            if char == "(":
                A.append("(")

            elif char == "[":
                A.append("[")

            elif char == ")":
                a = A.pop()
                if a != "(":
                    A.append("NO")
                    break

            elif char == "]":
                b = A.pop()
                if b != "[":
                    A.append("NO")
                    break
    except IndexError:
            answer.append('no')
    else: # 에러가 안뜨면 실행
        if len(A) == 0: #
                answer.append('yes')
        else: # [')',')']식으로 남아있는 경우 No
                answer.append('no')
for ans in answer:
    print(ans)