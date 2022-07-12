# 처음 시작 값
n = 0
# 0부터 더하기 위해서
total = 0
# user_input 값
user_input = int(input())

while n <= user_input:
    total += n
    n += 1
print(total)

# 순서에 따라 < or <= 가 달라진다. 
n = 0
total = 0
while n < user_input:
    n += 1
    total += n
print(total)

