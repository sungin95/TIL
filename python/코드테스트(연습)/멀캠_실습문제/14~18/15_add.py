"""
문자열 word가 주어질 때, 해당 문자열에서 a 의 모든 위치(index)를 출력해주세요.
find() index() 메서드 사용 금지
"""
word = 'HappyHacking'
findd = 'a'
count = -1
for i in word:
    count += 1
    if i == findd:
        print(count)
