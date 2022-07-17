from genericpath import samefile
import json
from pprint import pprint
from unittest import result

# 파일을 열고, 
kospi = open('stocks.json', 'r', encoding='utf-8')
# JSON을 파이선 객체 형식으로 한다!
json.load(f)
samsung = kospi['stocks'][0]
pprint(samsung, type(samsung))

# stockName 정보랑, closePrice 정보만 가진 딕셔너리를 만들고 싶어요!
result = {
    'stockName': samsung.get('stockName'),
    'closePrice': samsung.get('closePrice')
}
print(result)