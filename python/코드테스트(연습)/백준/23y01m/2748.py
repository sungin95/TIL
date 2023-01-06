N = int(input())
fibonacci_number = [0, 1]
if N == 1:
    print(fibonacci_number[1])
else:
    for i in range(1, N):
        next_ = fibonacci_number[i - 1] + fibonacci_number[i]
        fibonacci_number.append(next_)
    else:
        print(fibonacci_number[-1])
