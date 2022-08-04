T = int(input())
x = "1"
for t in range(T):
    a,b = input().split()
    
    if a == x: 
        x = b
    elif b == x:
        x = a
print(x)