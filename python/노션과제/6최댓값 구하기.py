numbers = [0, 20, 100]
max = 0
n = len(numbers)

for i in range(n-1):
    if(numbers[i]>numbers[i+1]):
        max = numbers[i]
        numbers[i+1] = max
        print(max)
    else:
        max = numbers[i+1]
        print(max)
