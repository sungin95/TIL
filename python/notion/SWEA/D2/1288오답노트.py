import sys
sys.stdin = open("1288.txt", "r")
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    N1 = N
    numbers = set()
    
    while True:

        for n in str(N):
            numbers.add(n)

        if len(numbers) == 10:
            break
        N += N1
    print(f"#{test_case} {N}")







"""
0~9까지 세는 방법은
리스트로 0,1 체크 하는 방법도 있다. index 활용가능(일반적인 방법)
or set(내가한 방법) 길이가 10이 되게 하기(파이썬 특징)
그리고 내가 한 방법과 비교해 보면.
세트 사용방법에 대한 생각 차이가 있다. 
나는 N -> KN(N의 K배) -> str(KN)을 m에 대입(이게 좀 불필요하네.)-> m 을 문자열에 넣고 그걸 세트에 넣었는데.
쌤은 N -> N += N1 -> str(N) -> 세트에 add(n)
그러니까. 
나는 k배 하기 위해 카운터까지 했는데. 그걸 줄였고
(N1 = N나는 이 과정에서 문제가 생길거라고 생각했는데. 
N값이 input에 의해 새롭게 정의되어서 내가 생각한 문제가 안나타났던거 같다. 
생각만 하지 않고 확인하는 습관이 이래서 중요한가 보다 )
문자열을 저장하고 그걸 세트에 넣었는데 문자열 과정을 생략하고 바로 add를 통해 세트에 넣어줬다. 
이 부분은 그냥 나의 코드 클린화가 실패한 것으로 보인다. 
"""