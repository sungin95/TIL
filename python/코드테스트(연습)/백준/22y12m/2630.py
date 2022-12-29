import sys

sys.stdin = open("2630.txt", "r")

N = int(input())
board = []
for i in range(N):
    data = input().split()
    board.append(data)

# 하얀과 파랑 색 카운트
cnt = [0, 0]

# 문제를 풀기 위해서는 함수가 필요하다고 느끼었다.
# 그리고 무엇을 사용하여 나눌것인가에 대해 고민을 해 보다가
# 그냥 숫자로 나누는 것이 가장 편할 거 같아서
# sy(y시작점), ey(y끝점), sx(x시작점), ex(x시작점)
def half(sy, ey, sx, ex):
    # set을 사용한 이유는 계속 추가되는거 막을려고
    white_check = set()
    blue_check = set()
    # 이중 for문을 사용하여 y,x표현
    for y in range(sy, ey):
        for x in range(sx, ex):
            # 파랑인지 하얀인지 체크
            if board[y][x] == "1":
                blue_check.add("check")
            else:
                white_check.add("check")
            # 섞여 있으면 4개로 나눈다.
            if blue_check & white_check == {"check"}:
                my = (ey + sy) // 2
                mx = (ex + sx) // 2
                half(sy, my, sx, mx)
                half(my, ey, sx, mx)
                half(sy, my, mx, ex)
                half(my, ey, mx, ex)
                # 작업 끝
                return

    # 섞여 있지 않으면 카운트
    else:

        if white_check == set():
            cnt[1] += 1
            print(sy, ey, sx, ex, "blue")
        else:
            cnt[0] += 1
            print(sy, ey, sx, ex, "white")


half(0, N, 0, N)
print(cnt[0])
print(cnt[1])
