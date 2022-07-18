"""

- 과일 데이터 `fruits.txt`를 활용하여 `berry`로 끝나는 과일의 갯수와 목록을 `02.txt`  에 기록하시오.
    - 과일은 하나당 한 줄에 기록되어 있습니다.

18
Honeyberry
Blackberry
Gooseberry
Juniper berry
Cranberry
Salal berry
Goji berry
Salmonberry
Bilberry
Cloudberry
Huckleberry
Raspberry
Mulberry
Elderberry
Marionberry
Strawberry
Boysenberry
Blueberry

"""
countt = 0
listt = []
with open('data/fruits.txt', 'r', encoding='utf-8') as f:
    for line in f:
        fruits_list = line.strip()
        f_berry = fruits_list[-5:]
        if f_berry == 'berry':
            listt.append(fruits_list)
    set_fruits = set(listt)
    list_fruits = list(set_fruits)
    with open('02.txt', 'w', encoding='utf-8') as f2:
        n = len(list_fruits)
        for i in range(n):
            f2.write(list_fruits[i]+"\n")
            countt += 1
        f2.write(str(countt))   
#    with open('01.txt', 'w', encoding='utf-8') as f2:
#        f2.write(str(countt))
    