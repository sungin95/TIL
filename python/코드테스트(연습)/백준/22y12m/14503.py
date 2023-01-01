import sys

sys.stdin = open("14503.txt", "r")

# 가장 어려웠던 점
# 문제를 읽고 순서를 어떻게 해야 하는 건지가 너무 어려웠다.
# 혹시 다른 분들은 어떻게 했는지 궁금하다.

# 기본 세팅
N, M = map(int, input().split())
r, c, d = map(int, input().split())

# 방에 벽 설치하기
room = []
for _ in range(N):
    data = input().split()
    room.append(data)

# 이 문제는 어느 방향에서 시작하는지가 매우 중요합니다.
# 북 동 남 서
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

# 0 빈칸, 1 벽, 2 청소한 구역

# cnt를 리스트로 해 줘야 함수에서 조작이 가능하다.
# 값 보정을 위해 1에서 시작
cnt = [1]

# 한칸씩 움직이며 청소
def move(r, c, d):
    room[r][c] = "2"
    # 현재 방향의 왼쪽부터 청소
    for i in range(3, -1, -1):
        di = (d + i) % 4
        nr = r + dy[di]
        nc = c + dx[di]
        # 청소를 안했으면
        if room[nr][nc] == "0":
            move(nr, nc, di)
            cnt[0] += 1
            break
    # 4방면 청소가 필요없으면
    else:
        di = (d + 2) % 4
        nr = r + dy[di]
        nc = c + dx[di]
        # 벽이 아니면
        if room[nr][nc] != "1":
            move(nr, nc, d)
        # 벽이면 끝
        else:
            return


move(r, c, d)
print(cnt[0])
