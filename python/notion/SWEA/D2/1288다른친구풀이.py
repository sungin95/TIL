import sys
sys.stdin = open("1288.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    numbers = [0] * 10
    
    count = 1
    while 0 in numbers:
        num = str(N * count)
        for i in range(len(num)):
            numbers[int(num[i])] += 1 # 이게 딕셔너리랑 같은 거구나. 
            print(numbers)
        count += 1
    print(f'#{test_case} {num}')

"""
구조가 리스트에 0을 채운 다음. 숫자 예를 들어 1955라면, 
'1955' -> for을 통해 1 9 5 5 를 numbers[1],numbers[9],numbers[5],numbers[5]의 방식으로 구현
그리고 각각에 1을 더해서 리스트에서 0이 사라지면 멈춘다. 

"""