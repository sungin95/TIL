S = input()
num_list = []
num = ""
for n in S:
    if n == "-" or n == "+":
        num_list.append(int(num))
        num = ""
        num += n
    else:
        num += n
else:
    num_list.append(int(num))

minus = False
answer = 0
for i in num_list:
    if minus == False and i >= 0:
        answer += i
    else:
        minus = True
        answer -= abs(i)
print(answer)
