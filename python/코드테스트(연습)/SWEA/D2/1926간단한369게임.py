import sys
sys.stdin = open("1926.txt", "r")

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

N = int(input())
n = 0
while N != n:
    m = ""
    n += 1
    str_n = str(n)
    for i in str_n:
        if i == '3' or i == '6' or i == '9':
            m += "-"
    if m == "":
        print(n, end=" ")
    else:
        print(m, end=" ")
