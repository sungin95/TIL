num = -10

if num >= 0:
    value = num
else:
    value = -num
print(num, value)

# 위 식과 같음.
value = num if num >= 0 else -num
# 핵심은 else인듯 하다. 대체로 특정 조건일때 그대로 가다가 아닐경우 else로 한다. 
# 를 표현하고 싶은거 같다. 
# 절대 복잡하게 쓸 식은 아니다. 