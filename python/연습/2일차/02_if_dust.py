dust_range = int(input())
# dust가 150보다 크면, 매우 나쁨
if dust_range > 150:
    print("매우나쁨")
# 80보다 크면, 나쁨
elif dust_range > 80:
    print("나쁨")
# 30보다 크면, 보통
elif dust_range > 30:
    print("보통")
# 좋은
# else는 위의 모든 조건에 해당하지 않는 나머지의 경우이기에 별도의 조건은 불가능
# 조건문에서 else는 생략이 가능하다. 
else:
    print("좋음")
