# 도미노
import sys

sys.stdin = open("3.txt", "r")
from itertools import combinations

domino_dict = {}
n = int(input())
for _ in range(n):
    p, h = map(int, input().split())
    domino_dict[p] = h
# m개를 뺄때
m = int(input())

# print(domino_dict, m)
keys = list(domino_dict.keys())
m_keys = combinations(keys, len(keys) - m)

# print(keys)
max_dainger = []
for k in m_keys:
    # print(k)
    # m개를 뺀 domino
    domino_dict_m = {}
    for key in k:
        domino_dict_m[key] = domino_dict[key]
    # print(k)
    m_dainger = 0
    for key in k:
        dainger = 0
        stack = []
        stack.append(key)
        visited = set()
        while stack:
            cur = stack.pop()
            visited.add(cur)
            for c in range(cur, cur + domino_dict_m[cur] + 1):
                # print(cur, domino_dict_m[cur], c)
                if domino_dict_m.get(c) != None and c not in visited:
                    stack.append(c)
                    dainger += 1
        # print("max", dainger)
        if m_dainger < dainger:
            m_dainger = dainger
    max_dainger.append(m_dainger)
print(min(max_dainger))
