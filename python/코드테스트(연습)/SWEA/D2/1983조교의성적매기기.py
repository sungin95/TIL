import sys

sys.stdin = open("1983.txt", "r")
T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split()) # 문제의 길이
    student_score = 0
    student_score_list = []

    for i in range(N): # 점수 합산 과정
        Midterms, finals, assignments = map(int,input().split())
        student_score = (Midterms * 35) + (finals * 45) + (assignments * 20)
        student_score_list.append(student_score)

    K_score = student_score_list[K-1]
    student_score_sort = sorted(student_score_list)
    rate = (student_score_sort.index(K_score))//(N//10)+1 # 올림처리 해야 한다. 
    score_rating = (["A+","A0","A-","B+","B0","B-","C+","C0","C-","D0"])
    score_rating.reverse() # 리스트 순서를 반대로 적었다.
    print(f"#{test_case} {score_rating[rate-1]}")
    