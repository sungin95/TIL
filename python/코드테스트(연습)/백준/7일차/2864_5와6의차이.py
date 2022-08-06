import sys
sys.stdin = open("2864.txt", "r")

A, B = input().split()
A_ = ""
B_ = ""
for i in A:
    if i == "6":
        i = "5"
    A_ += i
for j in B:
    if j == "6":
        j = "5"
    B_ += j
print((int(A_)+ int(B_) ),end=" ")
A_ = ""
B_ = ""
for i in A:
    if i == "5":
        i = "6"
    A_ += i
for j in B:
    if j == "5":
        j = "6"
    B_ += j
print((int(A_)+ int(B_) ),end=" ")