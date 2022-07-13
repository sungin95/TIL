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



# 나랑 다르네?

numbers = [ -10, -100, -30]

max_num = numbers[0]

for n in numbers:

    if max_num < n:

        max_num = n

print(max_num)

# 쌤은 리스트를 하나씩 비교를 하여 값이 더 큰게 나올 때 마다 바꾸는 방식을 택했다. 
# 나보다 더 깔끔하게 나왔다. 