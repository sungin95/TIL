students = ['이영희', '김철수', '이영희', '조민지', '김철수', '이영희', '조민지', '이영희']
n = len(students)
can_num = 0
count = 1

for i in range(1):     # i는 0이상 1미만의 값을 넣어주므로 반복문의 효과가 없이 i=0대입 후 종료됩니다.
    can_num += 1       # 1번만 실행 됩니다
    count = 1          # 1번만 실행 됩니다
    for j in range(can_num, n):
        if students[i] == students[j]:
            print(n)
            count += 1
            students.pop(j)
            print(students)
            j -= 1     # if 문 종료 후 for문들 돌면서 j는 range 에서 값을 새로 정의합니다. 
                    # 의미가 없을거 같아요!그리고 j값을 줄이지 않아도 pop되면서 해당 인덱스에 다른 문자가 위치하게  되므로 안적는게 맞는거 같아요! 
                    # 결과를 보면 세번째 이영희 삭제 후 다름 이영희 까지 통과가 두 번 떠야 하는데 한 번만 떴어요! 
                    # range에서 j에 그 다음 숫자를 입력하게 되고 결국 줄어든 리스트에서 한 명은 뛰어 넘고 그 다음 사람으로 넘어갑니다. 
                    # 그래서 마지막 이영희 삭제하고 인덱스 에러가 나는 것 같아요.
            n -= 1    
        else:
            print("통과")