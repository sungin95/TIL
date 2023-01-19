s = "banana"
str_dict = {}
text = ""
answer = 0
for st in s:
    if text == "":
        text = st
        str_dict[text] = 1
        str_dict["order"] = 0
    else:
        if text == st:
            str_dict[st] += 1
        else:
            str_dict["order"] += 1
            if str_dict[text] == str_dict["order"]:
                answer += 1
                text == ""
print(answer)
