import sys
sys.stdin = open("1936.txt", "r")

A, B = map(int,input().split())

if (A - B) ==  1:
    if A > B:
        print("A")
    else:
        print("B")
else:
    if A > B:
        print("B")
    else:
        print("A")
