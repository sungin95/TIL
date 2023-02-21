from heapq import heappop, heappush

N, K = map(int, input().split())

heapqueue = [(0, N)]
visited = [False for i in range(100021)]
visited[N] = True
if N < K:
    while heapqueue:
        time, location = heappop(heapqueue)
        if location == K:
            print(time)
            break
        if 0 < location < 100010:
            # 맨 처음으로 간 곳을 True처리 하기 때문에 적은 시간 순으로 구현해 주어야 한다.
            # 곱2를 해 줄때 인덱스를 벗어나는 경우가 있어서 Try 구문 사용
            try:
                # 순간이동
                if visited[location * 2] == False:
                    heappush(heapqueue, (time, location * 2))
                    visited[location * 2] = True
            except:
                pass
            # 한칸 걷기
            if visited[location + 1] == False:
                heappush(heapqueue, (time + 1, location + 1))
                visited[location + 1] = True
            # 한칸 뒤로 걷기
            if visited[location - 1] == False:
                heappush(heapqueue, (time + 1, location - 1))
                visited[location - 1] = True
        elif 0 == location:
            heappush(heapqueue, (time + 1, location + 1))
            visited[location + 1] = True
else:
    print(N - K)
