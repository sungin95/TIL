import sys
sys.stdin = open("1288.txt", "r")
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    k = 1
    KN = 0
    write_N = set()
    len_set_N = 0
    while len(write_N) != 10:
        KN = N*k
        k += 1
        for i in str(KN):
            write_N += i
    print(f"#{test_case} {KN}")

