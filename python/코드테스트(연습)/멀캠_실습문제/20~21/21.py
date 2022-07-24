number = 123123
number10 = number*10 # 계산을 위한 상수 
number_div = []
cnt = 0
answer = 0

while (number10 // 10) != 0:
    number10 = number10//10
    number_div.append(number10%10)
    cnt += 1

for i in range(cnt):
    answer += number_div[i]*(10**(cnt-1))
    cnt -= 1
print(answer)