from collections import deque


def solution(ingredient):
    cnt = 0
    ingredient = deque(ingredient)
    check = False
    rest = deque()
    while True:
        if check == False:

            for i in range(len(ingredient)):
                i = 0
                if (
                    i + 3 <= len(ingredient)
                    and ingredient[i] == 1
                    and ingredient[i + 1] == 2
                    and ingredient[i + 2] == 3
                    and ingredient[i + 3] == 1
                ):
                    cnt += 1
                    ingredient.popleft()
                    ingredient.popleft()
                    ingredient.popleft()
                    ingredient.popleft()
                    if len(rest) > 4:
                        for j in range(4):
                            b = rest.pop()
                            ingredient.appendleft(b)
                    else:
                        ingredient = rest + ingredient
                        rest = deque()
                    break
                a = ingredient.popleft()
                rest.append(a)
            else:
                check = True
        else:
            break
    answer = cnt
    return answer
