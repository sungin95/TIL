A = list(map(int, input().split()))
B = list(map(int, input().split()))

socore_A = 0
socore_B = 0
winner = "D"
for i in range(10):
    if A[i] > B[i]:
        socore_A += 3
        if socore_A >= socore_B:
            winner = "A"
    elif A[i] < B[i]:
        socore_B += 3
        if socore_A <= socore_B:
            winner = "B"
    elif A[i] == B[i]:
        socore_A += 1
        socore_B += 1
print(socore_A, socore_B)
print(winner)

    