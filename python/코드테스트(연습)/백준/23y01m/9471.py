import sys

sys.stdin = open("9471.txt", "r")

m = int(input())
check_list = []
for i in range(m):
    data1, data2 = map(int, input().split())
    check_list.append([data1, data2])

fibo = [0, 1]
print(1234)
for i in range(1, 500000):
    a = fibo[i - 1] + fibo[i]
    fibo.append(a)

print(123)
answer_list = []
for check in check_list:
    check__ = False
    fibo_rest = []
    for fi in fibo:
        if check__ == False:
            rest_fi = fi % check[1]
            fibo_rest.append(rest_fi)
            if len(fibo_rest) % 2 == 0 and len(fibo_rest) > 4:
                aaa = len(fibo_rest) // 2
                for j in range(aaa):
                    if fibo_rest[j] == fibo_rest[j + aaa]:
                        pass
                    else:
                        break
                else:
                    check__ = True
                    answer_list.append((check[0], aaa))
                    print(answer_list)
        else:
            break
print(answer_list)
