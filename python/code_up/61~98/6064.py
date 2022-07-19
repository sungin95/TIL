# a,b,c = input().split()
# a = int(a)
# b = int(b)
# c = int(c)
# m = 0
# if a < b:
#     m = a
# elif a >= b:
#     m = b
# elif c < m:
#     m = c
# elif c >= m:
#     pass
# print(m)
# vscode에서는 문제가 없는데 문제가 있다....

a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)
mix = ((a if a<b else b) if ((a if a<b else b)<c) else c)
print(mix)