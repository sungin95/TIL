import sys
sys.stdin = open("1976.txt", "r")
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    a, b, c, d = map(int, input().split())

    hour = a + c
    minute = b + d
    if hour >= 12:
        hour -= 12
    if minute >= 60:
        hour += 1
        minute -= 60
    print(f"#{test_case} {hour} {minute}")
