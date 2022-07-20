import sys
sys.stdin = open("2071.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
h = 0
for test_case in range(1, T + 1):
	a = input().split()
	n = 0
	for i in a:
		i = int(i)
		n += i
	b = (n / 10)
	h += 1
	print("#%d %d"% (h, round(b)))