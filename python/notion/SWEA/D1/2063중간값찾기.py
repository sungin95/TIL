import sys

sys.stdin = open("2063.txt", "r")
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

n = int(input())
m = ((n + 1)//2)-1
numbers = map(int, input().split())
num_list = list(numbers)
num_list.sort()
print(num_list[m])


# 문제는 못풀었다. 문제가 이상하다. 중간 값을 찾으라고 해서 199개중 100번째 값을 찾았는데 
# 답이랑 위치가 한참 떨어져 있었다. 

# 값을 정령을 해 주어야 한단다.... 문제 이해가 어렵네ㅠㅠ