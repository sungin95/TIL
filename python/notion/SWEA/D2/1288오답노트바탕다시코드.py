import sys
sys.stdin = open("1288.txt", "r")
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    N1 = N
    write_N = set()
    while len(write_N) != 10:
        N += N1
        for i in str(N):
            write_N.add(i)
    print(f"#{test_case} {N}")

