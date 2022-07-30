afterimage = input()
afterimage_rev = reversed(afterimage)
cnt_a = 0
cnt_b = 0
for char in afterimage:
    if char == '@':
        cnt_a += 1
    elif char == '=':
        pass
    else:
        break
for char   in afterimage_rev:
    if char == '@':
        cnt_b += 1
    elif char == '=':
        pass
    else:
        break
print(cnt_a, cnt_b)