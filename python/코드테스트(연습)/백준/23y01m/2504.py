import sys

sys.stdin = open("2504.txt", "r")

parenthesis = list(input())
stack = []
# 점수(정답)
score = 0
# 점수 계산 보조 변수
score2 = 1
# 이 문제의 핵심은 점수 누적 구조를 만들고 누적된 점수를 어느 타이밍에 더해 갈 것인가를 풀어야 했던 문제였다.
for i in range(len(parenthesis)):
    p = parenthesis[i]
    if p == "(":
        stack.append(p)
        score2 = score2 * 2
    elif p == "[":
        stack.append(p)
        score2 = score2 * 3
    else:
        if p == ")":
            if not stack or stack[-1] == "[":
                print(0)
                break
            # ((()())) 이런 상황이라면 4번째 상황과 6번째 상황에서 점수를 누적시킨 값을 점수에 추가 시켜준다.
            if parenthesis[i - 1] == "(":
                score += score2
            score2 = score2 // 2
        elif p == "]":
            if not stack or stack[-1] == "(":
                print(0)
                break
            if parenthesis[i - 1] == "[":
                score += score2
            score2 = score2 // 3
        stack.pop()

else:
    # 괄호 짝이 안맞으면
    if stack:
        print(0)
    else:
        print(score)
