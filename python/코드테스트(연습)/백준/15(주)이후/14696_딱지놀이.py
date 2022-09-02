t = int(input())
answer_list = []
for _ in range(t):
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A_ = A[1:]
    B_ = B[1:]
    A_.append(0)
    B_.append(0)
    A_.sort()
    B_.sort()
    i = -1
    try:
        while True:
            if A_[i] != B_[i]:
                if A_[i] > B_[i]:
                    answer_list.append("A")
                else:
                    answer_list.append("B")
                break
            i -= 1
    except:
        answer_list.append("D")
for ans in answer_list:
    print(ans)