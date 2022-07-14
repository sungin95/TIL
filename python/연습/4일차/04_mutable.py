# 리스트는 mutalble
a = [1, 2, 3]
a[0] = 100
print(a)
# [100, 2, 3]

# 문자열은 immutable
a = 'hi'
a[0] = 'c'
print(a)
"""
Traceback (most recent call last):
File "C:\Users\dlrke\OneDrive\문서\GitHub\국비지원학원\TIL\python\연습\4일차\04_mutable.py", line 9, in <module>
    a[0] = 'c'
TypeError: 'str' object does not support item assignment
"""