
T = int(input())
answer_list = []
for t in range(T):
    N, M = map(int,input().split())
    answer = 0
    for i in range(N,M+1): # 해당 범위의 수를 str로 변환해줘 하나하나 카운터해주고 모두 더했습니다. 
        answer += (str(i)).count("0")
    answer_list.append(answer)
for ans in answer_list:
    print(ans)
