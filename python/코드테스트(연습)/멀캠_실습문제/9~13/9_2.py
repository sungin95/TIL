students = ['이영희', '김철수', '이영희', '조민지', '김철수', '조민지', '이영희', '이영희']
candy = set(students) # students 리스트를 집합으로 변환하면서 중복을 제거한다.
print(candy)

stu=list(candy) # 집합 candy를 다시 리스트로 변환한다.

n = len(students)
m = len(stu)
count = 0

for i in range(m):
    count = 0
    for j in range(0, n):
        if stu[i] == students[j]:
            count += 1
            students.pop(j)
            students.insert(0,'1')
            print(students)
    print(count, stu[i])