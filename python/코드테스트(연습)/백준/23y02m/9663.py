n = int(input())

row = [0] * n
answer = 0


# 왼쪽 위 검증 함수
def is_check(x):
    for i in range(x):
        # 열체크 or 대각선 체크
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    return True


def n_queen(x):
    global answer
    # 체스판 끝까지 다 채우면 카운트
    # 모든 가로에는 반드시 퀀이 한개 있어야 하니까
    if x == n:
        answer += 1
        return
    else:
        # 모든 체스판에 퀀 한번씩 올려 보기
        # 한줄에 한개라도 올려야 다음으로 넘어간다.
        for i in range(n):
            row[x] = i
            if is_check(x):
                n_queen(x + 1)


n_queen(0)
print(answer)
