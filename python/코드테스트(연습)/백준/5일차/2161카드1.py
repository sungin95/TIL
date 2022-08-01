from collections import deque

n = int(input())
card = deque(range(1, n + 1)) # 덱 생성

while len(card) > 1: # 1개 남을 때 까지
    print(card.popleft(), end=" ") # popleft는 메소드이다. 
    card.append(card.popleft())

print(card[0])