"""
두 수를 Input으로 받아 합을 구하는 코드이다.
코드에서 오류를 찾아 원인을 적고, 수정하세요.
"""
numbers = input().split()
li_numbers = []
try:
    for num in numbers:
        num = int(num)
        li_numbers.append(num)
except ValueError:
    print('숫자를 입력해 주세요')
else:
    print(sum(li_numbers))
finally:
    print('계산이 끝났습니다.')

"""
문제는 input이 값을 문자열로 반환하는데. sum은 수치형을 받는다. 
그리고 문자열을 입력했을 때 사용자에게 무엇이 잘못되었는지 알려주지 못했다. 
"""