N = int(input())

t = [1]

for n in range(1, N + 1):
    i = -1
    j = n
    tn = 0
    while j != 0:
        i += 1
        j -= 1
        tn += t[i] * t[j]
    t.append(tn)
print(t[-1])
