"""
과일 데이터 fruits.txt를 활용하여 과일의 이름과 등장 횟수를  03.txt 에 기록하시오.


Boysenberry 3
Blueberry 4
Avocado 1
Marionberry 3
Date 9
...
Melon 1
berryfake 1


"""

result = {}
with open('data/fruits.txt', 'r', encoding='utf-8') as f:
    for line in f:
        result[line] = result.get(line, 0) + 1
    with open('03.txt', 'w', encoding='utf-8') as f2:
        for key in result:
            f2.write(key.strip()+ " " + str(result[key])+"\n")