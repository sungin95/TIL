m = int(input())


def k(m):
    km = []
    for i in range(2, m**2, 2):
        km.append(i)
    return km


n_list = k(m)

for n in n_list:
    a = k(2**n)
    ## 안풀음
