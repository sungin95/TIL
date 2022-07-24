"""
아래 코드는 1부터 N까지의 숫자에 2를 곱해서 변수에 저장하는 코드입니다.
코드에서 오류를 찾아 원인을 적고, 수정하세요.
"""
"""
N = 10
answer = ()
for number in range(N + 1):
    answer.append(number * 2)

print(answer)
"""
N = 10
answer = []
for number in range(1,N + 1):
    answer.append(number * 2)

print(answer)

# 우선 answer이 튜플형태라서 값을 추가할 수가 없었다. 이걸 리스트로 고쳐주었고,
# 1부터 N까지인데, 0이 저장이 되고 있어서 range(1:)을 주어서 1부터 시작하게 하였다. 
# Output [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20] 이라 써 있지만 내 생각에는 조건과 맞지 않아서 수정