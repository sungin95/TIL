a1 = int(input())
a2 = int(input())
a3 = int(input())
a4 = int(input())
a5 = int(input())
a6 = int(input())
a7 = int(input())
a8 = int(input())
a9 = int(input())
a_list = [a1,a2, a3, a4,a5,a6,a7,a8,a9]
sum_ = sum(a_list)
add_tall = sum_ -100
check = False
for i in range(8):
    if check == False:
        for j in range(i+1,9):
            if (a_list[i]+ a_list[j]) == add_tall:
                a_list.pop(j)
                a_list.pop(i)
                a_list.sort()
                check = True
                break
for ans in a_list:
    print(ans)