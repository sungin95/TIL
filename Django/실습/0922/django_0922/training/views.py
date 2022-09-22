from copy import copy
from django.shortcuts import render
import random
# Create your views here.


def today_dinner(request):
    what_eat_next = [['삼겹살', 'https://post-phinf.pstatic.net/MjAyMDAzMDNfMTcg/MDAxNTgzMTkwNjA3ODQ5.kUXPHqGJ2xPDSu_3FiEoFC3kY9QyQ_g9CziCGrFSDuEg.LpCfOTbc5qth9d-GKzGv9jwj2VKhcqmPHp5cp1KJYEsg.JPEG/IM_food02.jpg?type=w1200'],
                     ['치킨', 'https://upload.wikimedia.org/wikipedia/commons/2/20/Korean_fried_chicken_3_banban.jpg'], ['곱창', 'http://gdimg.gmarket.co.kr/1638958859/still/600?ver=1639450670']]
    decide = random.choice(what_eat_next)
    context = {
        'food': decide[0],
        'image': decide[1],
    }
    return render(request, "today-dinner.html", context)


def lotto(request):
    numbers = []
    lucky_numbers = []
    lotto_num = [3, 11, 15, 29, 35, 44]
    for i in range(1, 46):
        numbers.append(i)
    for _ in range(5):
        lucky_number = random.sample(numbers, 6)
        bonus = False
        cnt = 0
        for i in range(6):
            if lucky_number[i] in lotto_num:
                cnt += 1
            if 10 in lucky_number:
                bonus = True
        else:
            if cnt == 6:
                cnt = "1등"
            elif cnt == 5 and bonus == True:
                cnt = "2등"
            elif cnt == 5:
                cnt = "3등"
            elif cnt == 4:
                cnt = "4등"
            elif cnt == 3:
                cnt = "5등"
            elif cnt <= 2:
                cnt = "꽝"
            lucky_number.insert(0, cnt)
            lucky_numbers.append(lucky_number)

    lotto_numbers = {
        'first': lucky_numbers[0],
        'second': lucky_numbers[1],
        'third': lucky_numbers[2],
        'fourth': lucky_numbers[3],
        'fifth': lucky_numbers[4],
    }
    return render(request, 'lotto.html', lotto_numbers)
