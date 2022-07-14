
import random


numbers = [70, 170, 100, 50, 40, 30, 172, 54, 20, 56]
n = len(numbers)



for i in range(5):
    a = random.randrange(0,n)
    print(numbers[a])
    numbers.pop(a)
    n -= 1

