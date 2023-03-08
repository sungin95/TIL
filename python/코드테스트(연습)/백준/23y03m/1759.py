import sys

sys.stdin = open("1759.txt", "r")
from itertools import combinations


L, C = map(int, input().split())
str_list = input().split()

str_set = {"a", "e", "i", "o", "u"}

str_consonants = []
str_vowels = []
for s in str_list:
    if s in str_set:
        str_vowels.append(s)
    else:
        str_consonants.append(s)

answer_list = []
for i in range(1, len(str_vowels) + 1):
    for sv in list(combinations(str_vowels, i)):
        if L - i >= 2:
            for sc in combinations(str_consonants, L - i):
                answer = list(sv + sc)
                answer.sort()
                answer_str = ""
                for a in answer:
                    answer_str += a
                answer_list.append(answer_str)

answer_list.sort()
for a in answer_list:
    print(a)
