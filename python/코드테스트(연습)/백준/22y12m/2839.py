N = int(input())
cnt = 0

a = N // 5
cnt = a
b = N % 5
while b != 0:
    if b >= 3:
        b -= 3
        cnt += 1
    else:
        if a > 0:
            a -= 1
            b += 2
        else:
            cnt = -1
            break


print(cnt)
