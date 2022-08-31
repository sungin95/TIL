K = int(input())
def multiple_of_three (K):
    global K_list
    global cnt
    global answer
    K_list = list(str(K))
    answer = 0
    for k in K_list:
        answer += int(k)
    if K < 10:
        return answer
    else:
        cnt += 1
        multiple_of_three(answer)
cnt = 0
answer = 0
multiple_of_three(K)
print(cnt)
if answer%3 == 0:
    print("YES")
else:
    print("NO")