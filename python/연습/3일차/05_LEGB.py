sum = 5
print(sum([1, 2, 3]))

# Traceback (most recent call last):
#   File "C:\Users\dlrke\OneDrive\문서\GitHub\국비지원학원\TIL\python\연습\3일차\05_LEGB.py", line 2, in <module>
#     print(sum([1, 2, 3]))
# TypeError: 'int' object is not callable

# sum이 지금은 5가 되어버림...ㅠㅠ
# Built-in scopedp sum 함수가 있었음.
# Global scope에 sum이름의 변수를 만들었음.
# 제가 찾으니까 L -> E -> G -> B

name = '홍길동'

def add(a, b, c, name):
    return a + b + c
# 지역변수를 만들거나 인자를 받을 수 있게 만들거나. 