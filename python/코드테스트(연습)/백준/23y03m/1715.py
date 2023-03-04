from heapq import heappop, heappush

N = int(input())
card = []
for _ in range(N):
    data = int(input())
    heappush(card, data)
answer = 0
while len(card) != 1:
    card1 = heappop(card)
    card2 = heappop(card)
    heappush(card, card1 + card2)
    answer += card1 + card2

print(answer)
