contest_list = []
for _ in range(20):
    a = int(input())
    contest_list.append(a)
contest_W = contest_list[:10]
contest_K = contest_list[10:]
contest_W.sort()
contest_K.sort()
answer = []
print(sum(contest_W[7:]),(sum(contest_K[7:])))

