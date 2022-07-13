students = ['이영희', '김철수', '이영희', '조민지', '김철수', '조민지', '이영희', '이영희']
candy = {'이영희', '김철수', '이영희', '조민지', '김철수', '조민지', '이영희', '이영희'}
print(candy)
stu = []
stu.append(candy)
print(stu)

"""

stu = ['이영희', '김철수', '조민지']
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
            print(j,n, students)
    print(count, stu[i])

"""

# 후보를 따로 설정해 주지 않으면 작동을 안한다. 

