"""
소문자로 구성된 문자열 word가 주어질 때, 모두 대문자로 바꾸어 표현하시오.
.upper(), .swapcase() 사용 금지
"""
word = 'banana'
new_word = ''

for i in word:
    a = ord(i)
    a -= 32
    b = chr(a)
    new_word += b
    

print(new_word)



"""
### 파이썬 활용

특정 문자에 대응 되는 유니코드 숫자로 반환하는 함수는 `ord` 이다.

[https://docs.python.org/ko/3/library/functions.html#ord](https://docs.python.org/ko/3/library/functions.html#ord)

```python
ord('a') 
# 97
```

해당 유니코드 숫자를 문자로 반환하는 함수는 `chr`이다. 

[https://docs.python.org/ko/3/library/functions.html#chr](https://docs.python.org/ko/3/library/functions.html#chr)

```python
chr(97)
# 'a'
```"""