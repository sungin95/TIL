T = int(input())
company_dict = {}
key_list = []
for i in range(T):
    name, status_ = input().split()
    company_dict[name] = status_
keys = company_dict.keys()
for key_ in keys:
    if company_dict[key_] == "enter":
        key_list.append(key_)
answer = reversed(sorted(key_list))
for ans in answer:
    print(ans)
