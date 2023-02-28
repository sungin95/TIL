# 도미노
import sys

sys.stdin = open("3.txt", "r")
from itertools import combinations

# 도미노의 위치를 키 값으로, 높이를 밸류로 받았습니다.
domino_dict = {}
n = int(input())
for _ in range(n):
    p, h = map(int, input().split())
    domino_dict[p] = h
# m개를 뺄때
m = int(input())
# print(domino_dict, m)

# m개를 뺀 경우를 조합으로 표현
keys = list(domino_dict.keys())
m_keys = combinations(keys, len(keys) - m)

# max_dainger - m_dainger - dainger
# m_keys - k - key
max_dainger = []
for k in m_keys:
    # print(k)

    # m개를 뺀 domino 다시 정의(새롭게 정의 한걸로 사용한다.)
    domino_dict_m = {}
    for key in k:
        domino_dict_m[key] = domino_dict[key]

    #
    m_dainger = 0
    for key in k:
        # stack구조를 사용한 이유는 도미노가 추가적으로 넘어질 수 있고 아닐 수 있었는데.
        # 이걸 선택적으로 추가 할 수 있는 구조가 필요했음.
        dainger = 0
        stack = []
        stack.append(key)
        visited = set()
        while stack:
            cur = stack.pop()
            visited.add(cur)
            for c in range(cur, cur + domino_dict_m[cur] + 1):
                # print(cur, domino_dict_m[cur], c)
                # 넘어진 도미노에 닿은 도미노가 있는지 그리고 이 도미노는 이미 넘어진 도미노인지
                if domino_dict_m.get(c) != None and c not in visited:
                    stack.append(c)
                    dainger += 1
        # print("max", dainger)
        if m_dainger < dainger:
            m_dainger = dainger
    max_dainger.append(m_dainger)
print(min(max_dainger))
