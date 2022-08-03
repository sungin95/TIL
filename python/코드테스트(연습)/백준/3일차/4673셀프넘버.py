def d(x): # x 는 int 
    a = 0
    for i in str(x):
        a += int(i)
    y = x + a
    return y
N = {}
n = 10000
for i in range(1, n + 1): # 모든 수 0
    N[i] = 0
for i in range(1, n + 1): # 생성자는 있는 수는 1
    N[d(i)] = 1
for i in range(1, n + 1): # self number 출력
    if N[i] == 0:
        print(i)

  


