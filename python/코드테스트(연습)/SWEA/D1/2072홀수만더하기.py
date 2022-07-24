import sys
sys.stdin = open("2072.txt", "r")
t = 0
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
	a = map(int, input().split())
	t += 1
	answer = 0 
	for i in a:
		if i % 2 == 1:
			answer += i
	print(f"#{t}",answer)