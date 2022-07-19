# 얕은 복사

a = [1, 2, 3]
b = a 
b[0] = 'hi'
print(a)
# ! b가 바뀌었지만 a도 바뀌었다. 
print("========1")
# list 형변환
c = [3, 4, 5]
d = list(c)
d[0] = 'hi'
print(c)
print(d)
# ? 형변환을 하면 값 연동이 풀린다. 
print("========2")
# 슬라이싱 
e = [4, 5, 6]
f = e[::]
f[0] = 'hi'
print(e)
print(f)
# ? 인덱스를 하면 값 연동이 풀린다. 
print("========3")
# 깊은 복사
a = [[1, 2], 2, 3]
b = list(a)
b[0][0] = 'hi'
print(a) # [[1,2],2,3] or [['hi',2],2,3]
print(b) # [['hi',2],2,3]
# 리스트를 리스트하면 바뀌는게 없다
# ! 안안에 있는 것을 바꾸면 형변환을 해도 연동이 된다. 
print("========4")
import copy
c = [[1, 2], 2, 3]
d = copy.deepcopy(c)
d[0][0] = 'hi'
print(a)
print(b)
