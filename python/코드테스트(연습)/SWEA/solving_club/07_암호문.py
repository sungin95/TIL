import sys
sys.stdin = open("07.txt", "r")
t = 10
for test_case in range(1, t + 1):
    _ = input()
    answer = ""
    first = list(map(int, input().split()))

    insert_n = int(input())
    xys_all = input().split('I')

    for j in range(1,insert_n+1):
        xys = list(reversed(list(map(int, xys_all[j].split()))))
        for i in range(xys[-2]):
            first.insert(xys[-1], xys[i])
    for i in range(10):
        answer += f"{str(first[i])} "
    print(f"#{test_case} {answer}")

    


