T = int(input())
answer_list = []

for t in range(T):
    str_data = input().split()

    str_data_atad =[]
    for str_ in str_data: # 문자열 거꾸로하기.
        str_data_atad.append(str_[::-1])

    str_answer = ""
    for str_ in str_data_atad: # 리스트 => 문자열로 바꾸기.
        str_answer += (str_+" ")

    answer_list.append(str_answer) # 정답 모으기
for ans in answer_list:
    print(ans)