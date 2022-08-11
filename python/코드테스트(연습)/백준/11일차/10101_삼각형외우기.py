a= int(input())
b= int(input())
c= int(input())
abc = {a,b,c}
if a + b + c == 180:
    if len(abc) == 1:
        print("Equilateral")
    elif len(abc) == 2:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")