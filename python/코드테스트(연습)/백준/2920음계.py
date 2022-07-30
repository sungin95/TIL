a = map(int, input().split())
b = ''
for i in a:
    b += str(i)
if b == "12345678":
    print('ascending')
elif b == "87654321":
    print('descending')
else:
    print('mixed')