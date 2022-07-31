N = int(input())
cnt = 0
if N < 100: # 2자리수 이하는 모두 한수이다. 
    answer = N
    

else:
    list_i = []
    list_hansu = []
    answer = 99 + (((N//100) -1)*5) 
    handred = N//100
    n = (9-handred)//2
    for i in range(-1,(n-5),-1):# list_i == [-1,0,1,2,3]
        list_i.append(i)        # i의 값이 양수와 음수 모두 있어 for문 2개와 range를 이용하였다. 
    for i in range(n+1):
        list_i.append(i)

    for i in list_i: # list_i값을 이용해 한수를 만들고, N이 한수를 포함하면 카운트를 해 주었습니다. 
        handred = N//100
        hansu = f'{str(handred)+str(handred+i)+str(handred+(2*i))}'
        if N >= int(hansu):
            cnt += 1

answer += cnt
print(answer)