from ntpath import join
from unittest import result


word = "apple"

result_ = ""
for char in word:
    result_ = char + result_


print(result_)

# 나는 range로 거꾸로 배열시켜서 했는데... 이런 잡기술이 있는줄 생각을 못했네.

print(word[::-1])

# 이런것도 있네. 

print(''.join(reversed(word)))

# 이건 아직 이해를 못하겠네.

# 3. index
word = 'apple'

for i in range(len(word)):
    print(word[len(word)-i-1], end='')

# end가 단어를 다 모아주네?
# end ('\n')이 기본값인데 이걸 바꾸어준 것이다. 
# sep (' '): 여러개를 동시에 출력할 때 사이에 구분값.
