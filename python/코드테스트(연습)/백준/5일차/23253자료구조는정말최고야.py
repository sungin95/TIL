# 다른 분들이 한 거에서 힌트를 얻어
# if book_dumi[i] - before_value > 0:   
# [5 4 3 2 1]처럼 순차적으로 작아지면 통과
# [5 3 4 2 1]처럼 값이 꼬이면 check_ = False를 줘
# 거기서 계산을 멈추고 'No'를 프린트 하게 만들었습니다.
# https://discord.com/channels/992078696477372477/1003564754230583336/1003565066592976966


import sys
input = sys.stdin.readline # 자꾸 시간 초과 뜨는데. 이 두줄쓰니까 해결되었습니다. 
# 자세한 내용은 위 링크(자유qa채널에 있음) 참고

N, M = map(int, input().split())
book_dumiss = []
check_ = True
for m in range(M):
    n = int(input())
    book_dumi = (list(map(int, input().split())))
    if check_ == True: # check된게 없으면 계속 계산
        before_value = 222222 # 200000 첫 비교값 무조건 음수여야 한다. 
        for i in range(n):
            if book_dumi[i] - before_value > 0:
                check_ = False # 체크
                break
            before_value = book_dumi[i]
        
if check_ == True:
    print('Yes')
elif check_ == False:
    print('No')

"""
선생님 코드는 그 체크 하는 부분을 while과 pop을 사용하여 비교해 주었다. 
"""
