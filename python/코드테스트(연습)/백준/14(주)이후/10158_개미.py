import sys
sys.stdin = open("10158.txt","r")

w,h = map(int, input().split())
x,y = map(int, input().split())
t = int(input())
t_x = t%(2*w)
t_y = t%(2*h)
dy = [1,-1]
dx = [1,-1]
cnt_x = 0
cnt_y = 0
for i in range(t_x):
    x += dx[cnt_x%2]
    if x == 0 or x == w:
        cnt_x += 1
for i in range(t_y):
    y += dy[cnt_y%2]
    if y == 0 or y == h:
        cnt_y += 1
print(x,y)