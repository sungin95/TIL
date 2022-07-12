numbers = [10, 20, 100]
min = 0
n = len(numbers)

for i in range(n-1):
    if(numbers[i]<numbers[i+1]):
        min = numbers[i]
        numbers[i+1] = min
        print(min)
    else:
        min = numbers[i+1]
        print(min)
