# 이 문제는 처음에 많이 헤매다가 
# 넓이 1을 (1,1)과 같은 한개의 좌표랑 같다고 생각을 하고 문제를 풀었습니다. 
# 그래서 계산하는 범위의 좌표들을 리스트로 set로 모았고,
# 모두 한 set로 문제를 해결했습니다. 
# (처음에는 set계산식 하나하나 다 써 봤다가 무지성으로 그냥 다 합쳤는데. 답이 나왔습니다. )
# 다 풀고 보니 식은 상당히 간단했습니다.  

a = set()

for _ in range(4):
    I,J,X,Y = map(int, input().split())
    for x in range(I,X): # I부터 X까지 
        for y in range(J,Y): # J부터 Y까지 
            a.add((x, y))
print(len(a))
