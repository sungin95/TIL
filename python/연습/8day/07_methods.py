# 함수 내부에서 값을 쓰고 싶으면 어떻게 해야하죠?
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
