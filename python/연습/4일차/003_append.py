from unittest import result


a = [1, 2, 3]
a = a.append(4)
# 코드의 결과는 무엇일까요?
# a.append(4)의 return 값을 a에 저장한다. 
# 리스트.append()의 메서드는 반환값이 None임!
print(a)

a = [1, 2, 3]
a.append(4)
print(a)
# 리스트는 변경가능

a = [1, 2, 3]
# sum 함수의 return 값을 result에 할당
result = sum(a)
# 문자열은 변경 불가능