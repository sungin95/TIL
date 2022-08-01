# 문제를 읽다보니 값이 순서대로 올라가고 있었고, 
# 곱해야 하는 값도 한자리, 두자리, 세자리 이런 식으로 늘어나서
# 인덱스를 이용해 해당 위치 값을 통해 문제를 풀면 되겠다고 생각했습니다.  
color_list = ['black','brown','red','orange','yellow','green','blue','violet','grey','white']

a = input()
b = input()
c = input()
a_ = color_list.index(a)
b_ = color_list.index(b)
c_ = color_list.index(c)
answer = int(str(a_)+str(b_)+('0'*c_))

print(answer)
