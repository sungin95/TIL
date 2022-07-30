import sys
sys.stdin = open("05.txt", "r")
t = int(input())
for test_case in range(1, t + 1):
    odd_number = 0
    even_number = 0
    answer = 0
    a,b,c,d,e,f,g,h,i,j,k,l,n,m,o = map(int, input().split())
    odd_number = ( a + c + e + g + i + k + n + o)*2
    even_number = ( b + d + f + h + j + l + m)
    N = odd_number + even_number
    answer = (10 -(N % 10)) % 10

    print(f"#{test_case} {answer}")