# 소는 10마리 
# 관찰횟수 N번
# 위치는 왼쪽과 오른쪽 (0,1)로 표현.
# 이 관찰 기록을 가지고 소가 최소 몇 번 길을 건넜는지 알아보자. =>처음 확인했는 때는 노카운트
# 즉 같은 번호의 소가 위치를 바꾼 것이 몇 번인지 세면 된다.
N = int(input())
cow_dict = {} # 처음에 소를 발견하면 카운트는 하지 않으면서 위치를 기록해 줘야 했습니다.
# 이걸 리스트로 하면 매우 복잡할거 같지만, 딕셔너리를 사용하면 get을 사용하면 끝나는 문제이기 때문에.
# 딕셔너리를 사용하여 문제를 풀었습니다.  
cnt = 0
for _ in range(N):
    cow_N, left_right = input().split() 
    if cow_dict.get(cow_N) == None: # 최초로 확인했을 때는 카운트를 하지 않는다. 
        cow_dict[cow_N] = left_right # 위치 정보만 기록
    elif cow_dict[cow_N] != left_right: # 위치 기록이 다를때
        cow_dict[cow_N] = left_right # 위치를 바꾸어 기록해 주고 
        cnt += 1 # 카운터를 해 준다. 
print(cnt)

"""
9
3 1
3 0
6 0
2 1
4 1
3 0
4 0
3 1
3 0
"""