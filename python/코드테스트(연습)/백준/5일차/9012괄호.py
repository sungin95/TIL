# 이 문제는 .pop할때 값이 없으면 자꾸 에러가 떠서 힘들었습니다.
# 그래서 try 문을 사용하였습니다.  

T = int(input())
for t in range(T):
    PS = input()
    VPS_check = []
    try:    
        for ps in PS:
            if ps == '(':
                VPS_check.append('(')
            else:
                VPS_check.pop()
    except IndexError: # .pop 할 값이 없어 에러가 뜨면 No프린트
        print('NO')

    else: # 에러가 안뜨면 실행
        if VPS_check == []: #
            print('YES')
        else: # [')',')']식으로 남아있는 경우 No
            print('NO')

