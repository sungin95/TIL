answer_list = []
N = int(input())
for _ in range(N):
    A, B = input().split()
    if len(A) != len(B):
        answer_list.append([A,B,False])
        continue
    a_list = []
    b_list = []
    for a in A:
        a_list.append(a)
    for b in B:
        b_list.append(b)
    a_list.sort()
    b_list.sort()
    for i in range(len(A)):
        if a_list[i] != b_list[i]:
            answer_list.append([A,B,False])
            break
    else:
        answer_list.append([A,B,True])
for ans in answer_list:
    if ans[2] == True:
        print(f"{ans[0]} & {ans[1]} are anagrams.")
    else:
        print(f"{ans[0]} & {ans[1]} are NOT anagrams.")

