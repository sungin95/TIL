
# 문제: 은민이는 4와 7을 좋아하고, 나머지 숫자는 싫어한다. 금민수는 어떤 수가 4와 7로만 이루어진 수를 말한다.
# N이 주어졌을 때, N보다 작거나 같은 금민수 중 가장 큰 것을 출력하는 프로그램을 작성하시오.

# 문제 접근. 
# 처음에는 while을 이용하여 1씩 감소 시키는 방식을 고민하였지만, 수가 커질 수록 연산량이 너무 커진다고 생각을 하였습니다. 
# 제 생각은 좋은 코드는 코드가 짧은 것보다는 연산과정이 짧아야 한다고 생각했습니다. 
# 그 결과 해당 수를 가장 큰 자리에서 작은 자리로 이동을 하며, 해당 조건에 맞는지를 파악하는 방식으로 문제를 풀게 되었습니다.  

# 
N = input() # 해당 값을 문자로 받았습니다. 
N_list = [] # 그리고 그 문자를 하나하나 쪼개서 리스트로 만들어 줬습니다.  
for char in N:
    N_list.append(char)
print(N_list) # 예시
n = len(N)

for i in range(n): # N_list[i] 값은 ['0','1','2','3','4','5','6','7','8','9']
    if int(N_list[i]) == 4 or int(N_list[i]) == 7: # 숫자가 4,7이면 통과 남은건 ['0','1','2','3','5','6','8','9']
        pass
    else: # 4,7이 아니면 
        if int(N_list[i]) > 7: # 7이상인지 확인, 남은건 ['0','1','2','3','5','6'] 예시 8858
            print(N_list, N_list[i], i)
            N_list[i] = "7"
            for j in range(i+1,n):
                N_list[j] = "7"
            else:    
                break
        elif int(N_list[i]) > 4: # 4 이상인지 확인, 남은건 ['0','1','2','3'] 예시 5858
            print(N_list, N_list[i], i)
            N_list[i] = "4"
            for j in range(i+1,n):
                N_list[j] = "7"
            else:
                break

        else: # 3이하이면 
            # 1. 앞자리 수를 바꾸거나 (이 경우 7일때만 4로 가능)
            # 2. 자릿수를 내려 주어야 합니다. 

            if i == 0: # 맨 앞자리가 0이면 성가셔서 따로 처리 해 주었습니다.   예시 1858
                print(N_list, N_list[i], i)
                N_list[i] = "0" # 0으로 바꾸고
                for j in range(1,n):
                    N_list[j] = "7" # 나머지를 7로 해 줍니다. 
                else:
                    break
            else: # 맨 앞자리가 아니면 
                for k in range(i-1,-1,-1): # 역으로 돌면서 7을 찾는다.  예시 4734
                    if N_list[k] == "7": # 7을 찾으면(있으면) 
                        print(N_list, N_list[i], i)
                        N_list[k] = "4" # 4로 바꾸고 
                        for j in range(k+1,n): # 그 뒤의 값 모두 7로 
                            N_list[j] = "7"
                        else:
                            break # 모두 바꾸면 끝
                else: # 만약 7이 없으면     예시 44434
                    print(N_list, N_list[i], i)
                    N_list[0] = "0"
                    for j in range(1,n):
                        N_list[j] = "7"
                    else:
                        break
answer =""
for ans in N_list:
    answer += ans
print(int(answer))
