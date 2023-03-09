import sys

sys.stdin = open("14003.txt", "r")


def sol():
    N = int(input())
    nums = [*map(int, input().split())]
    stack = [nums[0]]

    for i in nums[1:]:
        if stack[-1] < i:
            stack.append(i)
        else:
            for j, v in enumerate(stack):
                if i <= v:
                    stack[j] = i
                    break
    print(stack)
    return len(stack)


print(sol())
