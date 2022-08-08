T = int(input())
answer_list = []
for t in range(T):
    answer = 0
    S = int(input())
    answer += S # 차 가격은 한번 계산
    T2 = int(input())
    for t2 in range(T2): # 옵션은 가격과 갯수 곱해주고 모두 합
        q,p = map(int, input().split())
        answer += q*p
    answer_list.append(answer)
for ans in answer_list:
    print(ans)