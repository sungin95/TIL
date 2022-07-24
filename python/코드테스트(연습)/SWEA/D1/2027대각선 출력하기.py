b = "#"
for i in range(5):
    a = ['+', '+', '+', '+']
    c = ""
    a.insert(i,b)
    for j in a:
        c += j
    print(c)