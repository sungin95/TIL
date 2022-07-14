"""
문자열 word가 주어질 때, 
Dictionary를 활용해서 해당 문자열에서 등장한 모든 알파벳 개수를 구해서 출력하세요.
"""
from itertools import count
# Deduplication 중복 제거

word = "banana"

list_word = [] 
for i in word:
    list_word.append(i) 
# print("list_word" ,list_word)

dict_list_ = {}
for i in list_word:
    dict_list_[i] = 0 
# print("dict_list_", dict_list_)

Dedu_list = list(dict_list_)
# print("Dedu_list",Dedu_list)

n = len(Dedu_list)


def dict_input_count(n):
    for i in range(n):
        count_ = list_word.count(Dedu_list[i])
        dict_list_[Dedu_list[i]] = count_

def each_other_print():
    for i in Dedu_list:
        print(i,dict_list_[i])


dict_input_count(n)
each_other_print()

