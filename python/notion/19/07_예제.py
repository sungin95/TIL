"""
아래 코드는 평균을 구하는 논리적으로 오류가 있는 코드입니다. 
코드에서 오류를 찾아 원인을 적고, 수정하세요.
"""
"""
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0
count = 0

for number in number_list:
    total += number
count += 1

print(total // count)
"""
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0
count = 0

for number in number_list:
    total += number
    count += 1

print(total / count)

# 우선 count에 들여쓰기까 빠져 있어 수정을 했고
# //는 나눗값의 몫만 나타내는데. 
# 평균값을 구할려면 소수점 자리도 필요하다고 생각해서 /로 바꾸어 주었다. 