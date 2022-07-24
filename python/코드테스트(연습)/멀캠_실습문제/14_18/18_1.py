word = 'banana'

# 1. 풀이
result = {}
for char in word:
    # 딕셔너리에 키가 없으면?
    if not char in result:
        # 키랑 값을 1으로 초기화한다.
        result[char] = 1
    # 딕셔너리에 키가 있으면?
    else:
        result[char] = result[char] + 1
print(result)


result = {}
for char in word:
    # result['a'] 없으면 KeyError
    # result.get('a') 기본값이 None
    # result.get('a', 0) 기본값이 0
    result[char] = result.get(char, 0) + 1
print(result)

# 출력부분
for key in result:
    print(key, result[key])

"""
몰랐던것: 
1. in을 사용하여 딕셔너리에 키가 있는지 없는지 확인이 가능한지 몰랐다. 
=> 이것을 몰라서 
리스트 -> 딕셔너리 + 값 추가 -> 다시 리스트(중복이 사라진다.)
2. 더 쉬운 get을 몰랐다. 
=> 위 케이스 + count를 따로 만들어 횟수를 기록하여 따로 대입을 안해줘도 되었다. 
"""