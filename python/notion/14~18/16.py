"""
문자열 word가 주어질 때, 해당 문자열에서 모음의 갯수를 출력하시오.
모음 : a, e, i, o, u 
count() 사용 금지
"""

word = "zxcvb  "
findd = 'aeiou'
count = 0

for i in word:
    for j in findd:
        if i == j:
            count += 1
print(count)

"""
나는 이중 for문을 이용 했는데. if in : 이 방법으로도 해결 할 수있다. 
word=input()
cnt=0
for i in range(len(word)):
    if word[i] in ['a','e','o','u','i']:
        cnt+=1

print(cnt)
"""
    