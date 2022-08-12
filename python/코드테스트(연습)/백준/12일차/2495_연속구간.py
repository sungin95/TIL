answer_list = []
for i in range(3):
    num = input()
    cnt = 1
    consecutive_numbers = [1]
    for j in range(1,len(num)):
        if num[j-1] == num[j]:
            cnt += 1
        else:
            if cnt != 1:
                consecutive_numbers.append(cnt)
            cnt = 1
    else:
        consecutive_numbers.append(cnt)
    answer_list.append(max(consecutive_numbers))
for ans in answer_list:
    print(ans)
