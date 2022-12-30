# 왜 틀렸을까???


from collections import deque 


def make(ingredient, fo_ingredient):
    ingredient = deque(ingredient)
    fo_ingredient = deque()
    cnt = [0]
    while ingredient:
        i = 0
        if ingredient[i] == 1:
            if i+3 < len(ingredient) and ingredient[i+1] == 2 and ingredient[i+2] == 3 and ingredient[i+3] == 1:
                b = fo_ingredient.pop()
                for j in range(4):
                    ingredient.popleft()
                ingredient.appendleft(b)
                remaining_ingredients = ingredient
                cnt[0] += 1
                make(remaining_ingredients, fo_ingredient)
                break
        a = ingredient.popleft()
        fo_ingredient.append(a)

    make(ingredient, fo_ingredient)
    answer = cnt[0]
    return answer