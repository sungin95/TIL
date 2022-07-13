def no():
    a = 1

result = no()
print(result, type(result)) # None <class 'NoneType>

def foo():
    return 1, 2

result = foo()
print(result, type(result)) # 튜블로 묶어서 반환한다. 



# print 함수는
# 출력을 해주고, return 값은 없습니다. 
a = print('hi')
print(a, type(a)) # None <class 'NoneType>