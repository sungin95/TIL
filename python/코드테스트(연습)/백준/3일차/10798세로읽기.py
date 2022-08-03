a = input()
b = input()
c = input()
d = input()
e = input()
a_n = len(a)
b_n = len(b)
c_n = len(c)
d_n = len(d)
e_n = len(e)
answer = ""
max_n = max(a_n, b_n, c_n, d_n, e_n)
for i in range(max_n): # 큰 데이터를 다루지 않고 문자열의 길이 이상으로 프린트를 할려고 하면 에러가 나므로 if문을 여러개 사용하는 방식 사용했습니다. 
    if i < a_n:
        answer += a[i]
    if i < b_n:
        answer += b[i]
    if i < c_n:
        answer += c[i]
    if i < d_n:
        answer += d[i]
    if i < e_n:
        answer += e[i]
print(answer)
