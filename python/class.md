# 클래스

class에는 속성과 메소드가 있다.

```python
class Person:
    
    def __init__(self, name):# _가 2개해 주어야 한다. 
        self.name = name
    # 클래스 변수(속성)
    type = '싸람'
    species = '사람'

    # 인스턴스 메서드
    # 인스턴스가 활용할 메서드
    def greeting(self):
        print('안녕하세요~!')

iu = Person()
iu.greeting()

# 클래스 변수(속성)
print((Person.type))
print(Person.species)

# 지은: 안녕하세요~!
# 싸람
# 사람
```



## 객체 비교하기

- ==

```python
a = [1, 2, 3]
b = [1, 2, 3]
# 값은 같지만 저장주소가 다르다. 
print(a == b, a is b)
# True False
```

- is

```python
a = [1, 2, 3]
b = a
# 완전 동일하다. 
print(a ==b, a is b)
```

True True 

## 얕은 복사, 깊은 복사

```python
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
```



# 클래스 메소드,스태틱 메소드

```python
# 정의할 때 이름을 지어놓고, 호출할 때 값을 넘겨줘요!

class MyClass:
    class_variable = '클래스변수'
    
    # 메서드를 정의했습니다. 
    def __init__(self):
        self.instance_variable = '인스턴스 변수 '
        
    # 인스턴스 메서드
    def instance_method(self):
        return self
    
    # 클래스 메서드
    @classmethod # ! 핵심 
    # @는 데코레이터: 함수를 꾸며주는 것인데 우리 지금 보지 말아요.(장고에서 자세히)
    def class_method(cls):
        return cls
    
    # 스태틱 메서드 정의 
    @staticmethod # ! 핵심
    def static_method():
        return ''

c1 = MyClass()
print('인스턴스 변수 호출', c1.instance_variable)
print('인스턴스 메서드 호출', c1.instance_method())# c1
# self자동으로 받음
print('클래스 메서드 호출', c1.class_method())# MyClass
# 클래스 그 자체 필요한 경우
print('스태틱 메서드 호출', c1.static_method())
# 클래스 인스턴스 모두 필요가 없을 떄
# 절대 클래스 혹은 인스턴스를 사용 할 수 없다. 

# self, cls 예약어인가요? 
# 아니다. 관용적으로 사용하는 것이다. 
```

메소드 정리

- 인스턴스 메소드
  - 호출한 인스턴스를 의미하는 self 매개 변수를 통해 인스턴스를 조작
- 클래스 메소드
  - 클래스를 의미하는 cls 매개 변수를 통해 클래스를 조작
- 스태틱 메소드
  - 인스턴스나 클래스를 의미하는 매개변수는 사용하지 않음
    - 즉, 객체 상태나 클래스 상태를 수정할 수 없음
  - 일반 함수처럼 동작하지만 클래스의 이름공간에 귀속 됨
    - 주로 해당 클래스로 한정하는 용도로 사용



## 객체지향의 핵심개념

- 추상화
- 상속
  - super

- 다형성
- 캡슐화
  - 접근제어자(public, private 등 파이썬에서는 중요도가 떨어져서 다루지 않음)