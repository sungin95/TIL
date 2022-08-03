# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt")

a, b = input().split() # 두개 수 str로 받음

result = "" # 정의
for chr in (a): # 문자 거꾸로 받기 
    result = chr + result
a = int(result)

result = "" # 초기화
for chr in (b): # 2개만 처리 하면 되니까 그냥 반복해 주었다. 
    result = chr + result
b = int(result)

print(a) if a > b else print(b) # 3항식


# 다른 친구 풀이. 상당히 더 깔끔하다. 
# A, B = input().split()

# A = A[::-1] # 역순으로 정렬
# B = B[::-1]

# print(max(A, B))