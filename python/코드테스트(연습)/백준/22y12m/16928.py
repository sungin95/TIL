import sys

sys.stdin = open("16928.txt", "r")

N, M = map(int, input().split())

# 사다리 or 뱀 디셔너리 활용 구현
up_down_dict = {}
for _ in range(N + M):
    a, b = map(int, input().split())
    up_down_dict[a] = b

# 100은 안넘기겠지?
answer_list = [100]

# 잔가지를 줄이기 위해 디셔너리 활용
check = {}
for i in range(1, 101):
    check[i] = 10000

# 1~6칸 가는 모든 경우의 수 탐색
# 모든 경우의 수를 탐색하다 보니 시간이 너무 많이 걸렸다.
# 그래서 잔가지를 줄이는 것을 목적으로 코드를 주로 짰다.


def move(i, cnt):
    cnt += 1
    # 주사위 굴리는 최소 횟수니까
    if cnt < min(answer_list):
        # 역수를 사용한 이유는 조금이라도 시작을 줄일 수 있을까 해서
        for j in range(6, 0, -1):
            # 1~6의 경우의 수
            k = i + j

            # 사다리 or 뱀
            if up_down_dict.get(k) is not None:
                k = up_down_dict[k]

            if k < 100:
                # 딕셔너리를 활용하여 지나온 길의 주사위 던진 횟수가 적을때만 계산하도록 로직을 구성
                if check[k] >= cnt:
                    check[k] = cnt
                    move(k, cnt)
            # 도착하면 던진 횟수 체크
            elif k == 100:
                answer_list.append(cnt)


move(1, 0)
print(min(answer_list))


# while True:
#     if len(answer_list) == 1:
#         answer_list[0] += 1
#     else:
#         break
