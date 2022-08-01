import sys
input = sys.stdin.readline # 이게 뭔지는 모르겠지만 시간초과라고 뜨면 이걸 쓰면 해결이 된다. 

# 이 문제는 딕셔너리를 사용했는데. 이유는 참가자 리스트를 만들어야 하는데. 
# 정렬된 숫자가 아닌 사람이름으로(불규칙한) 값을 만들어야 하는데. 이때는 키를 이용하는 것이 편합니다. 
# 그리고 이름 중복이라는 문제를 해결하기 위해 이름 적을때 카운트, 완주자 체크할때 역카운트를 하여
n = int(input())
marathon_dict = {} # 딕셔너리 활용!
for i in range(n):# 우선 n명의 이름으르 적는다. 
    people = input()
    if marathon_dict.get(people) != None: # 동명이인이 존재하면 1씩 추가 
        marathon_dict[people] += 1
    else:
        marathon_dict[people] = 1 # 처음 이름적기

for i in range(n-1):# n-1은 문제 조건
    people = input()
    marathon_dict[people] -= 1 # 역카운트

for person in marathon_dict:
    if marathon_dict[person] != 0: # 완주자는 0이 되고, 비완주자는 1이 된다. 
        print(person)              # 0이 아니면 프린트.
        break # 이건 계산 과정을 줄이기 위해.

