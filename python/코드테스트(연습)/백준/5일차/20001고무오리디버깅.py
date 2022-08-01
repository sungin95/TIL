_ = input()
duk_list = []
while True:
    problem = input()
    if problem == '고무오리 디버깅 끝':
        break
    try:
        if problem == '문제':
            duk_list.append('문제')
        elif problem == '고무오리':
            duk_list.pop()
    except IndexError:
        duk_list.append('문제')
        duk_list.append('문제')
if duk_list == []:
    print("고무오리야 사랑해")
else:
    print("힝구")
