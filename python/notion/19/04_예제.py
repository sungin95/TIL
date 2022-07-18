"""
아래 코드는 문자열을 입력받아 단어별로 나누는 코드입니다.
코드에서 오류를 찾아 원인을 적고, 수정하세요.
"""
"""
words = list(map(int, input().split()))
print(words)
"""

# input은 문자열로 반환하는데 이걸 구지 수치형으로 변환하였고,
# split이 리스트형으로 반환하는데 이걸 구지 다시 리스트를 주었다. 

words = input().split()
print(words)