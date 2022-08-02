T = int(input())
answer = []
for t in range(T):
    ad_no, ad_fit, ad_cost = map(int, input().split())
    if ad_no < ad_fit - ad_cost:
        answer.append('advertise')
    elif ad_no > ad_fit - ad_cost:
        answer.append('do not advertise')
    else:
        answer.append('does not matter')
for ans in answer:
    print(ans)

