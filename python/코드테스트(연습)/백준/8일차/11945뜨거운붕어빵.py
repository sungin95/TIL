N, M = map(int, input().split())
fish_bun = [] # 붕어빵
for n in range(N):
    data = input()
    fish_bun.append(data[::-1]) # 문자열 뒤집어 저장
for ans in fish_bun: # 정답출력
    print(ans)