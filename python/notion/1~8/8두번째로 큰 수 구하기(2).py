numbers = [0, 20, 100, 0, 20, 1000, 20, 1000, 20, 100]
max = 0
max_second = 0
n = len(numbers)

for i in range(n-1):
    if(numbers[i]>numbers[i+1]):
        max = numbers[i]
        numbers[i+1] = max
        print(max_second)
        print(max)
    else:
        max_second = max
        max = numbers[i+1]
        print(max_second)
        print(max)

# 코드를 좀더 간결하게 변경