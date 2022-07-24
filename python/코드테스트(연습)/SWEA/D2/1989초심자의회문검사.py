import sys
sys.stdin = open("1989.txt", "r")
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    a = input()
    b = ''
    for i in a:
        b += i
        b += " "
    individual_char = b.split()
    n = len(individual_char)
    half = n//2
    true = 1
    for i in range(half):
        if individual_char[i] != individual_char[-i-1]:
            true = 0
    print(f"#{test_case} {true}")
