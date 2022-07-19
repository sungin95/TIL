t = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

for i in range(t):
    a, b = map(int,input().split())
    print("#%d %d %d"% (i+1, a//b, a%b))
