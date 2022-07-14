"""
문자열 word가 주어질 때, 해당 문자열에서 a 가 처음으로 등장하는 위치(index)를 출력해주세요.
a 가 없는 경우에는 -1을 출력해주세요.
find() index() 메서드 사용 금지
"""
a = 'apple '
findd = 'a'
count = -1
b = 1
for i in a:
    count += 1
    if i == findd:
        print(count)
        b = 0
        break
if b == 1:
    print(-1)

# 썜 풀이 보니까 for else 가 사용 가능하다. 
# 또는 b를 boolean형으로 만들어서 사용할 수도 있다. 