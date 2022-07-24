numbers = [3, 10, 20]
total = 0
nng = 0
for i in numbers:
    total += i
    nng += 1

aver = total / nng
print(aver)

# 내가 잘 몰랐던 부분이 for i in [리스트] 이 부분을 생각을 못하였다. 
# 그리고 aver의 위치를 위로 해서 한동안 애먹었다. 
# 파이썬은 오른쪽에서 위에서 → 왼쪽, 아래인데. 아직 익습하지 않았던거 같다. 