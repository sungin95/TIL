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



