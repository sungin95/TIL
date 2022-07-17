with open('test.txt', 'w',encoding = 'utf-8') as f:
    f.write("Happy Hacking!\n")
    for i in range(1, 6):
        f.write(f'{i} 번째!\n')