import sys
sys.stdin = open("2304.txt","r")

N = int(input())
warehouse_ab = []
warehouse = []
for _ in range(N):
    a,b = map(int, input().split())
    warehouse_ab.append([a,b])
warehouse_ab.sort()
for i in warehouse_ab:
    warehouse.append(i[1])

max_value = max(warehouse)
max_location = []
width = 0

max_middle = 0
location = [0]
for i in range(N):# 커지면 그 이전까지 너비 구하기 
    if max_middle < warehouse[i]:
        width += (max_middle* (warehouse_ab[i][0]-location[0]))
        location = []
        location.append(warehouse_ab[i][0])
        max_middle = warehouse[i]
        if max_middle == max_value:
            max_location.append(warehouse_ab[i][0])
            break

max_middle = 0
location = [warehouse_ab[N-1][0]]
for i in range(N-1,-1,-1): # 반대로 
    if max_middle < warehouse[i]:
        width += (max_middle* (location[0] - warehouse_ab[i][0]))
        location = []
        location.append(warehouse_ab[i][0])
        max_middle = warehouse[i]
        if max_middle == max_value:
            max_location.append(warehouse_ab[i][0])
            break
width += max_value*((max_location[1]+1) - max_location[0]) # 최대높이가 같을 경우 대비

print(width)


