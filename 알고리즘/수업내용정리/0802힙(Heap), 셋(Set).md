# 힙(Heap), 셋(Set)

힙

우선순위 큐![우선순위큐](0802힙(Heap), 셋(Set).assets/우선순위큐.JPG)





예시) 설문조사

롤키고 있을때 크롬을 킨다면

우선순위 큐 다양한 방식

그중 힙이라는 데이터를 활용하는 방식

힙을 우선운위 큐로 활용할 수 있는 데이터 구조이다. 

다른 방법은 O(N)인데 힙은 O(logN)이다. 

## 힙의 특징

최대값 또는 최소값을 빠르게 찾아내도록 만들어진 데이터구조 완전 이진 트리의 형태로 느슨한 정렬 상태를 지속적으로 유지 한다. 힙 트리에서는 중복 값을 허용한다.

## 힙은 언제 사용해야 할까

1. 데이터가 지속적으로 정렬되야 하는 경우(대충이나마)
2. 데이터에 삽입/삭제가 빈번할 때 

![힙과리스트비교](0802힙(Heap), 셋(Set).assets/힙과리스트비교-16594050479793.JPG)

![큐유](0802힙(Heap), 셋(Set).assets/큐유-16594050890916.JPG)

```python
import heapq

numbers = [5, 3, 2, 4, 1]

heapq.heapify(numbers) # 원본이 바뀐다. 어중간한 정렬상태를 유지한다. 

heapq.heappop(numbers) # 최소값 1이 나오고 어중간한 정렬상태를 유지한다. 

heapq.heappop(numbers)

heapq.heappush(numbers, 10)

heapq.heappush(numbers, 0)

print(numbers)
# heapq.heapify() 이건 pop, push과정에서 수행한다. 필수는 아니다. 
# heapq.heappop(heap)
# heapq.heappush(heap, item)
```





# 셋(Set)

집합



![셋](0802힙(Heap), 셋(Set).assets/셋-16594080182829.JPG)



## 셋의 연산

```
1) .add( ) 
2) .remove( ) 
3) + ( 합 ) 
4) - ( 차 ) 
5) & ( 교 ) 
6) ^ (대칭차 )
```

```python
print(len(set(words) & set(S)))
```



## Set은 언제 사용해야할까? 

1. 데이터의 중복이 없어야 할 때 (고유값들로 이루어진 데이터가 필요할때) 
2. 정수가 아닌 데이터의 삽입/삭제/탐색이 빈번히 필요할때







