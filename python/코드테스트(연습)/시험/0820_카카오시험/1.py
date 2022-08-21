def solution(new_id):
    step1 = new_id.lower()
    step2 = ""
    cnt = 0
    for s2 in step1:
        if ord(s2) == 95 or ord(s2) == 45 or ord(s2) == 46 or (97 <= ord(s2) and ord(s2) <= 122) or (48 <= ord(s2) and ord(s2) <= 57):
            if ord(s2) ==46:
                cnt += 1
            else:
                cnt = 0
            if cnt <= 1:
                step2 += s2

    if step2 == "" or step2 == ".":
        step2 = "a"
    if step2[0] == ".":
        step2 = step2[1:]
    if step2[-1] == ".":
        step2 = step2[:-1]

    step6 = ""
    N = len(step2)
    if N >= 15:
        N = 15
    for i in range(N):
        step6 += step2[i]
    if step6[-1] == ".":
        step6 = step6[:-1]
    if len(step6) <= 3:
        while len(step6) != 3:
            step6 += step6[-1]
    answer = step6
    return answer