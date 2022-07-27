# 생성자와의 차이는 무조건 N-(n*9) 그러니까 (자리수 * 9)값 이내라고 가정을 하고 풀었습니다. 

N = input()
n = len(N)
N = int(N)
b = False
range_ = N-(n*9)

if N < 18: # N이 17 이하부터는 제 공식의 값이 마이너스가 되어버려서 0으로 고정 시켰습니다. 
    range_ = 0

for i in range(range_, N): # 하나하나 대입하며 찾는 식
    a = 0
    for j in str(i):
        a += int(j)
    if N == i + a:
        print(i)
        b = True
        break
if b == False:
    print(0)


# for - else 를 활용 할 수도 있다. 