while True: # 계산식이 몇개인지는 알 수 없지만
    # 마지막에는 a,b각각 0이 나온다는 힌트가 있어서 while을 썻고, 
    # 해당값이 나오면 결과를 출력하지 않고 멈쳐야 해서 True break 구문을 사용하였다. 
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    else:
        print(a + b)