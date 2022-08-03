# 접근법: 1. 최대 공약수는 두 수의 차를 넘을 수 없다. 
# 2. 최소 공배수 = 최대 공약수 * a나머지 * b나머지

a, b = map(int, input().split())

a_b_absolute = a - b # a-b 절대값     1번 접근법
if a_b_absolute < 0:
    a_b_absolute = -(a_b_absolute)

greatest_common_divisor = 0
for i in range(a_b_absolute , 0, -1): # 두 수의 차이의 역수로 값을 찾아 주었습니다. 
    if (a % i == 0 and b % i == 0): # 최초로 두 값이 나누어 질 때, 값이 최대 공약수입니다. 
        greatest_common_divisor = (i) # 최대 공약수  
        a_rest = int(a/i) # a 나머지
        b_rest = int(b/i) # b 나머지
        break
if greatest_common_divisor == 0: # 위 식은 12 12 처럼 수가 같을때 작동하지 않습니다. 그래서 예외를 만들었습니다. 
    greatest_common_divisor = a
    a_rest = 1
    b_rest = 1

print(greatest_common_divisor) # 최대 공약수
print(greatest_common_divisor * a_rest * b_rest) # 최소 공배수

