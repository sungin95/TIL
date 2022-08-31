k = int(input())

def factory(count):
    global answer
    global k
    if count == k:
        return answer
    answer += (answer*count)
    count += 1
    factory(count)

answer = 1
count = 0
factory(count)
print(answer)
