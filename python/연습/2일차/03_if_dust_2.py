dust_range = -10

if dust_range > 150:
    if dust_range > 300:
        print("실외할동을 자체하세요.")
    print("매우나쁨")

elif dust_range > 80:
    print("나쁨")

elif dust_range > 30:
    print("보통")

else:
    if dust < 0:
        print('음수 값이니다.')
    else:
        print("좋음")
