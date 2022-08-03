# 이 문제의 핵심은 중복을 처리와 ENTER을 기준으로 리셋하고 다시 세는 것이다. 
# 우선 중복문제는 set을 이용하였다. 알다시피 중복이 되면 set은 알아서 다 제거해 준다.
# 그리고 ENTER가 나오면 .clear을 통해 리스트를 리셋 시켜 주었다.
# 그리고 방금 강사님의 수업을 통해 set.clear가 된다는 것을 알았다. 
# 그러니까 내 식의 리스트를 애초에 set으로 설정하여 식을 만들었으면 더 좋았을 거 같다.   

T = int(input())
answer = 0
message_list = []
for t in range(T):
    message_ = input()
    if message_ == 'ENTER':
        answer += len(set(message_list))
        message_list.clear()
    else:
        message_list.append(message_)
answer += len(set(message_list))
print(answer)

# set_.add(log)