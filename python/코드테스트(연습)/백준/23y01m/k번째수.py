def solution(array, commands):
    answer = []
    for command in commands:
        arr = array[command[0] - 1 : command[1]]
        arr.sort()
        answer.append(arr[command[2] - 1])
    return answer
