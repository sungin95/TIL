T = int(input()) 
company_dict = {} # 직원들이 출근한 상태인지 아닌지를 체크하는 가장 좋은 방법은 딕셔너리를 활용하는 것이었다. 
# True False를 이용할까 고민했지만 대상의 이름으로 기록을 하지 못한다. 
# 그에 반해 딕셔너리를 활용하면 입력된 이름을 통하여 이 사람이 상태를 바로바로 추가가 가능하고, 중복까지도 바로 제거가 가능하여 사용하였다. 
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
