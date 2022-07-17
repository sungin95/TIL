numbers = [0, 20, 100, 40]
max_number = float("-inf")
second_number = float("-inf")

# 1. 전체 숫자를 반복
for n in numbers:
    # 만약에, n이 최대보다 크다면
    if max_number < n:
        # 최대값이었던 것이 두번째로 큰 수
        second_number = max_number
        max_number = n
    # elif second_number < n < max_number:
    elif second_number < n and n < max_number:
        second_number = n
print(second_number)

"""
1. 나의 것과 비교했을때, 우선 float("-inf") 이 부분은 나도 있어야 했다. 
다시 보니 2번쨰는 아예 틀렸네. 
가장 큰 차이는 방식에 대한 접근 방식인거 같다. 
가장 큰 값이 바뀔때 두번째 큰 값도 변화를 시킨다. 이 부분에 대해서는 접근 방법이 같지만
2. 그 다음으로 신경을 쓸 부분은 max에는 변화가 없지만 두번째로 큰 값이 바뀌는거에 대한 방법인데. 
이 부분에 대해 제대로 신경을 못쓴듯 한다. 
첫번째 방법은 너무 많은 동작을 사용해서 좋은 코드라고 할 수 없고. 
기본적으로 하나하나 비교가 아니라 앞뒤 값을 비교하는 방식을 사용하여 제대로 신경을 못써준거 같다. 
"""