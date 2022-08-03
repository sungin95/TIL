import sys
sys.stdin = open("5533.txt", "r")
N= int(input())
numbers = []

for i in range(N): 
    list_2 = []
    data = list(map(int, input().split()))
    for j in data:
        list_2.append(j)
    numbers.append(list_2)    
M = len(data)
print(numbers)
b = {}
for i in range(M):
    a = []

    for j in range(N):
        a.append(numbers[j][i])
    print(a)
    

