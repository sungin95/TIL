names = ','.join(['홍길동','춘향이'])
print(names)
# 홍길동, 춘향이

# numbers = " ".join([10, 20, 100])
# 위 방법으로 하면 str가 와야 하는데 int가 와서 오류가 생긴다. 
numbers = ' '.join(map(str, [10, 20, 100])) # str 형변환하는 함수이지 함수가 아니다. 
print(numbers)
