first_num = int(input())
new_num = -1    
n = first_num
cnt = 0
while first_num != new_num:
    n = str(n)
    if int(n) < 10:
        n = "0" + n
    add_ = (int(n[0])+int(n[1]))
    if add_ >= 10:
        add_ = add_ % 10

    new_num = n[1] + str(add_)
    new_num = int(new_num)
    n = new_num
    cnt += 1
print(cnt)