a, b, c = map(int, input().split()) 
prize_money = 0
if a == b and a == c: # if문을 사용하여 푼 이유는 첫째로 처리해야 하는 데이터 양이 적었다. 
    # 둘째로는 경우의 수도 그렇게 다양하지 않았다. 만약 경우의 수가 10가지 씩 된다면 좀 더 좋은 
    # 방법을 찾아야 했겠지만 5가지 정도라서 그냥 편하게 if문을 사용해 주었다. 
    prize_money += 10000 + (1000*a)
elif a == b:
    prize_money += 1000 + (100*a)
elif a == c:
    prize_money += 1000 + (100*a)
elif c == b:
    prize_money += 1000 + (100*c)
else:
    max_ = max(a,b,c)
    prize_money = max_ * 100
print(prize_money)
