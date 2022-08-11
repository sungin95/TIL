str_input = input()
n = len(str_input)
cnt = 0
none_ = False
for i in range(n):
    if str_input[i] == ":":
        if str_input[i+1] == "-":
            if str_input[i+2] == ")":
                cnt += 1
                none_ = True
            elif str_input[i+2] == "(":
                cnt -= 1
                none_ = True
if none_ == False:
    print("none")
elif cnt > 0:
    print("happy")
elif cnt < 0:
    print("sad")
elif cnt == 0:
    print("unsure")
