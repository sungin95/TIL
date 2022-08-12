answer_list = []
for i in range(5):
    FBI = input()
    FBITRUE = FBI.replace("FBI", "") # replace는 return 값이 변하는 것이다. 
    n = len(FBI)
    m = len(FBITRUE)
    if n != m:
        answer_list.append(i+1)
if answer_list == []:
    print("HE GOT AWAY!")
else:
    for ans in answer_list:
        print(ans, end=" ")

