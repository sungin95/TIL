# 파일명, 어떤 모드로 열지,
# 인코딩을 설정
with open('test.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    print(text, type(text))

