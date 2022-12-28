def solution(price, money, count):
    pay = 0
    for i in range(count):
        pay += price
        money -= pay
    if money >= 0:
        money = 0
    else:
        money = abs(money)

    return money
