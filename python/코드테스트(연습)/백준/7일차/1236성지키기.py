import sys
sys.stdin = open("1236.txt", "r")
N, M= map(int, input().split())

numbers = []
hor = []# i를 활용하여 몇번째 세로 줄인지 확인.
vert = [] # cnt를 이용하여 몇번째 가로 줄인지 체크
for i in range(N): 
    cnt = 0
    data = input()
    for char in data:
        if char == "X":
            hor.append(i) # hor(x)에는 i(위치 인덱스와 같은 기능)을 저장한다. 
            vert.append(cnt) # vert(y)에는 cnt(위치 인덱스와 같은 기능)을 저장한다. 
        cnt += 1 # 위치(몇번째  가로 줄인지)를 알려주는 용도로 사용중.
a = N - (len(set(hor))) # 겹치는 위치 set를 통해 제거. 
b = M - (len(set(vert)))
print(max(a,b)) # 이중 큰 값이 최소 값이다. 
       


# import sys
# sys.stdin = open("1236.txt", "r")
# from pprint import pprint
# N, M = map(int, input().split())
# rectangle = []
# cnt = 0
# for i in range(N): 
#     list_2 = []
#     data = input()
#     if data.find("X") == -1:
#         cnt += 1
#     for j in data:
#         list_2.append(j)
#     rectangle.append(list_2)    
# cnt2 = 0
# for i in range(M):
#     a = []
#     for j in range(N):
#         a += (rectangle[j][i])
#     else:
#         try:
#             if a.index("X") == -1:
#                 pass
#         except:
#             cnt2 += 1
# print(max(cnt, cnt2))



# for n in range(k-1,k):  # 행과 열 확인 중복 x ㄱ 반대 모양으로 탐색. 
#     for m in range(k-1,M):
#         print(rectangle[n][m])
# for n in range(k,N):
#     for m in range(k-1,k):
#         print(rectangle[n][m])
# N, M = map(int, input().split())
# test = []
# rectangle = []
# K = min(N,M)
# X = []
# cnt = 0
# for k in range(K):
#     value = []
#     print()
#     for m in range(k,M):  # 행과 열 확인 중복 x ㄱ 반대 모양으로 탐색.
#         value.append(rectangle[k][m])
#     for n in range(k+1,N):
#         value.append(rectangle[n][k])
#     print(value)
#     try:
#         value.index("X")
#         a = False
#         b = False
#         if value[0] != "X":
#             for i in range(1, M-k):
#                 if i == "X":
#                     a = True
#             for j in range(M-k, len(value)):
#                 if j == "X":
#                     b = True
#             if a == False:
#                 print("문제 행.")
#                 for n in range(k+1,N):
#                     test.append(rectangle[n][k])
#             elif  b == False:
#                 print("문제 열")
#                 for m in range(k,M):  # 행과 열 확인 중복 x ㄱ 반대 모양으로 탐색.
#                     test.append(rectangle[k][m])
#     except:
#         rectangle[k][k] = "X"
#         print("X가 없으면 만들면 된다")
#         cnt += 1
# pprint(rectangle)
# print(cnt)
# print(test)



