import sys
sys.stdin = open("2025.txt", "r")

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
n = int(input())

m = 1
sum = 0
while n+1 != m:
    sum += m
    m += 1
    
print(sum)
