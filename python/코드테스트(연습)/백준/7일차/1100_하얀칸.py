import sys
sys.stdin = open("1100.txt", "r")


arr = []
for i in range(8):
    data = input()
    arr.append(data)
cnt = 0

for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0: # 하얀칸과 검은칸의 차이는 i+j%2 값이 1인지 0인지로 나눌 수 있다. 
            if (arr[i][j]) == "F":
                cnt += 1
print(cnt)
