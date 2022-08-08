# replace와 len의 길이를 통해 해결 
str_ = input()
find_str = input()

x = str_.replace(find_str,"")
n = len(find_str)
a = len(str_)
b = len(x)
answer = (a-b)//n

print(answer)

