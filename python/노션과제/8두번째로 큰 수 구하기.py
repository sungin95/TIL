numbers = [0, 20, 100, 50, -60, 50, 100] # 50
n = len(numbers) # 리스트 길이
c = 1 # 카운트
while(n >= c):
    c += 1
    print(numbers)
    for i in range(n-1):
        if(numbers[i]>numbers[i+1]):
            a = numbers[i]
            b = numbers[i+1]
            numbers[i] = b
            numbers[i+1] = a
else:
    print("====================")
    for i in range(n-1):
        if(numbers[-i-1]==numbers[-i-2]):
            print("이게 아니야")
        else:
            print(numbers[-i-2])
            break