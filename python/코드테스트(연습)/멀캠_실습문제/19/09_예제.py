"""
아래 코드는 과일의 개수를 구하는 논리적 오류가 있는 코드의 일부분 입니다.
코드에서 오류를 찾아 원인을 적고, 수정하세요.
"""
"""
from pprint import pprint

fruits = [
    "Soursop",
    "Grapefruit",
    "Apricot",
    "Juniper berry",
    "Feijoa",
    "Blackcurrant",
    "Cantaloupe",
    "Salal berry",
]

fruit_count = {}

for fruit in fruits:
    if fruit not in fruit_count:
        fruit_count = {fruit: 1}
    else:
        fruit_count[fruit] += 1

pprint(fruit_count)
"""
from pprint import pprint

fruits = [
    "Soursop",
    "Grapefruit",
    "Apricot",
    "Juniper berry",
    "Feijoa",
    "Blackcurrant",
    "Cantaloupe",
    "Salal berry",
]

fruit_count = {}

for fruit in fruits:
    if fruit not in fruit_count:
        fruit_count[fruit] =  1
    else:
        fruit_count[fruit] += 1

pprint(fruit_count)

# 위 식의 문제점은 계속 fruit_count = {}의 값이 새롭게 대입이 된다는 것이다.(추가를 해야 한다. )
# 딕셔너리 형식은 매우 편하게도  fruit_count["Soursop"] = 1 이렇게만 해 줘도 바로 추가가 된다는 것이다.
