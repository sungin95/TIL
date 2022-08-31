import math

answer = 0
t, k = map(int, input().split())
student_dict = {}
for _ in range(t):
    s, g = map(int, input().split())
    if student_dict.get((s,g)) == None:
        student_dict[(s,g)] = 1
    else:
        student_dict[(s,g)] += 1
for i in student_dict:
    answer += math.ceil(student_dict[i]/k)
print(answer)