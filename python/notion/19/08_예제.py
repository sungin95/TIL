"""
아래 코드는 문자열에서 모음의 개수를 찾는 코드입니다. 
코드에서 오류를 찾아 원인을 적고, 수정하세요.
"""
"""
word = "HappyHacking"

count = 0

for char in word:
    if char == "a" or "e" or "i" or "o" or "u":
        count += 1

print(count)
"""
word = "HappyHacking"

count = 0

for char in word:
    if char in "aeiou":
        count += 1

print(count)

# char == "a" or "e" or "i" or "o" or "u": 
# 이 식의 의도는 모음과 같으면 카운터 하라고 지었지만(사람이 보기에는 이상이 없어 보인다.)
# 파이썬은 "a" 이후에 모든 값을 True로만 인식한다. 
# ( a를 제거하면 if "e" or "i" or "o" or "u": 파이썬은 이렇게 인식한다. )
# 그래서 다른 방식으로 식을 고쳤다. 