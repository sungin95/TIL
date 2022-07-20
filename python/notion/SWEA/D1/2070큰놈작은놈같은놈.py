import sys
sys.stdin = open("2070.txt", "r")
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for t in range(1, T + 1):
    a, b = input().split()
    a = int(a)
    b = int(b)
    if a > b:
        print(f"#{t} >")
    elif a == b:
        print(f"#{t} =")
    elif a < b:
        print(f"#{t} <")