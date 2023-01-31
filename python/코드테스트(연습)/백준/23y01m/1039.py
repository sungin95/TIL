import sys

sys.stdin = open("1039.txt", "r")

N, K = input().split()
K = int(K)

for i in range(len(N)):
    for j in range(len(N)):
        if N[j] != "0":
            print(N[i], N[j])
