p,q,r,s,w = map(int, input().split())


a = (w * p)

if r >= w:
    b = q
else: 
    b = q + (s*(w-r))

if a <= b:
    c = a
else:
    c = b
print(c)

# print(f'#{test_case} {min(a,b)}')
# min이라는 게 있네???



