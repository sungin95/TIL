# 문제가 좀 상식적으로는 이해하기 힘든 문제였던거 같습니다. 
# 그러니까 문제가 
# 문제  누울수 있는 자리 
# ....X ....
# ..XX. ..
# ..... .....
# .XX.. ..
# X.... ....
# 세로(오른쪽으로 90도 회전)
# X.... .... 
# .X... ...
# .X.X.
# ...X. ...
# ....X ....
# 이렇게 .이 2개 이상이 나오면 누울수 있는 자리로 카운트 하여 
# 가로 세로 따로 값을 구하면 되는 문제입니다. 
import sys
sys.stdin = open("1652.txt", "r")

N = int(input())
arr = []
cnt_point = 0 # .의 갯수를 카운트
cnt_bed = 0 # 누울수 있는 자리. 
answer = 0
def check_bed(data):
    cnt_bed = 0
    cnt_point = 0
    for check in data: # 체크식
        if check == "X": # X를 만났을때
            if cnt_point >= 2: # ..이상이면 
                cnt_bed += 1 # 누울수 있는 자리 
            cnt_point = 0 # .갯수 초기화 
        else:    # .을 만났을때 
            cnt_point += 1 # . 갯수 카운트
    else: # 계산이 끝나면 
        if cnt_point >= 2: # 벽을 만났을때 ..이상이라면 
            cnt_bed += 1 # 누울수 있는 자리 하나 추가 
        cnt_point = 0 # .갯수 초기화 # 필요없긴 하다.
    return cnt_bed

for n in range(N): # 천번째 답
    data = input()
    arr.append(data) # 가로
    answer +=(check_bed(data))
print(answer,end=" ") # 가로 갯수 프린트

arr3 = [] # 90도 회전 배열 이름은 대충... 
for x in range(N):
    arr2 = []
    for y in range(N):
        arr2.append(arr[y][x])
    arr3.append(arr2) # 90도 회전 계산식.

answer =0 # 두번째 정답
for check2 in arr3: # 아까 input()이랑 같은 역할 
    data = check2
    answer +=(check_bed(data))
print(answer)

