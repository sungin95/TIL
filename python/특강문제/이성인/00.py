"""

아래의 내용을  00.txt에 기록하시오.

N회차 홍길동
Hello, Python!
1일차 파이썬 공부 중
2일차 파이썬 공부 중
3일차 파이썬 공부 중
4일차 파이썬 공부 중
5일차 파이썬 공부 중
"""

"""

# 'r' : read (읽기 전용)
# 'w' : write (쓰기 전용 - 덮어씀)
# 'a' : append (쓰는데 파일 있으면 이어서 씀)
with open('test.txt', 'w', encoding='utf-8') as f:
    f.write('Happy Hacking!\n')
    for i in range(1, 6):
        f.write(f'{i} 번째!\n')

"""

with open('00.txt', 'w', encoding='utf-8') as f:
    f.write('Hello, Python!\n')
    for i in range(1, 6):
        f.write(f'{i}일차 파이썬 공부 중\n')