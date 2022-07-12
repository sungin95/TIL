dust_range = -10


if dust_range > 150:
    print("매우나쁨")

elif dust_range > 80:
    print("나쁨")

elif dust_range > 30:
    print("보통")

elif dust_range > 0:
    print("좋음")

else:
    print('음수 값이니다.')

