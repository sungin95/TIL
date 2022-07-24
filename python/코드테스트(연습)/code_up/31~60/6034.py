a, b = input().split()
a = int(a)
b = int(b)
c = 0
def abs(a, b): 
    if a > b:
        c =a - b
        return c
    else:
        c = b - a
        return c 

print(abs(a,b))
# 틀렸다... 당연히 절대값을 주어야 한다고 생각했는데. 그게 틀렸다.
# 하지만 나의 정답이 이거니까. 남겨둔다. 