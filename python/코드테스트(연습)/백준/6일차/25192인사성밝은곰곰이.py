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