numbers = ['1', '2', '3']

# 숫자로 바꿔서 쓰고 싶다. 
# n = int(numbers)
# 리스트를 -> 숫자로 바꾸는 형변환 불가능 
# 다만, 숫자 형태의 문자를 변환할 수는 있습니다. 

# 가능! 100개, 1000개 일때는?
a = int(numbers[0])
b = int(numbers[1])
c = int(numbers[2])
new_numbers = [a, b, c]

# 반복문!
new_numbers = []
for number in numbers:
    new_numbers.append(int(number))
print(new_numbers)
# 우리의 마음 각각 적용시키고 싶었다. 

# map!
numbers = ['1', '2', '3']
new_numbers_2 = map(int, number) # <map object at 0x000002307C40FFA0>: dlal gkatnrk ahen wjrdyd ehldj dlTek. 
print(new_numbers_2, type(new_numbers_2)) # 
print(list(new_numbers_2)) 
# 리스트로 형변환해서ㅓ보면 바뀌어있다.~!
# 보기 위해서 바꾼 것일 ㅃ뿐! 반드시 list로 바꿔야하는 것은 아닙니다. :)


