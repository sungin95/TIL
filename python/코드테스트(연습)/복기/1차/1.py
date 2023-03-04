# 상희형 풀이
n = 7
mt = [7, 7, 7, 1, 1, 1, 7]

fall = 0
for i in range(n):
    if mt[i] > i * 2 + 1:
        fall += mt[i] - i * 2 - 1
        mt[i] = 2 * i + 1
    elif mt[i] < i * 2 + 1:
        if mt[i] + fall >= i * 2 + 1:
            fall -= i * 2 + 1 - mt[i]
            mt[i] = i * 2 + 1
        else:
            mt[i] += fall
            fall = 0
print(fall)
print(mt)
