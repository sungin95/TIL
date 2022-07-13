# 직사각형의 넓이를 구하시오.
# 직사각형 세로는 n 가로는 m
# Input 예시
# 10 20
import numbers


n, m = map(int, input().split())
print(n*m)
# 문자열.split() 내가 구분값을 기준으로 조개겠다.
# 반환결과는 항상 리스트 
# 전체 해석
# 문자열로 받을 것은 각각을 공백을 기준으로 리스트로 쪼겠다.
# => 리스트!!! ['10', '20']

# map
# 어떤 함수를 반복가능한 것들의 요소에 모두 적용시킨 결과!
# int함수를 input().split() 리스트의 모든 요소에 적용한 결과

# => map object (맵 어떤것)
# [10, 20]

# n, m = [10, 20]

# 내가 알던 int랑 이름만 같은가 보네. 

# 내장함수를 10을 다 더해주는 함수가 있어요.
def plus10(n):
    return n + 10

numbers = [10, 20, 30]
new_numbers =  list(map(plus10, numbers))
print(new_numbers)