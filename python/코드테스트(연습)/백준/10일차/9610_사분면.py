N = int(input())
answer_dict = {
    "Q1": 0,
    "Q2": 0,
    "Q3": 0,
    "Q4": 0,
    "AXIS": 0
}
answer_list = []
for n in range(N):
    x,y = map(int, input().split())
    if x > 0 and y > 0:
        answer_dict["Q1"] += 1
    elif x < 0 and y > 0:
        answer_dict["Q2"] += 1
    elif x < 0 and y < 0:
        answer_dict["Q3"] += 1
    elif x > 0 and y < 0:
        answer_dict["Q4"] += 1
    else:
        answer_dict["AXIS"] += 1
for ans in answer_dict:
    answer_list.append(answer_dict[ans])
print(f"Q1: {answer_list[0]}")
print(f"Q2: {answer_list[1]}")
print(f"Q3: {answer_list[2]}")
print(f"Q4: {answer_list[3]}")
print(f"AXIS: {answer_list[4]}")