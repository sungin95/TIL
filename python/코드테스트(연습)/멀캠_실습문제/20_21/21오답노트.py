number = 123

# print(int(str(number)[::-1]))

# ! 이전 나머지 결과에 10을 곱해준다.  

result = 0

while number:
    # 이전 결과에 10을 곱하고
    result *= 10
    # 나머지를 더해주고
    result += number%10
    # number를 깎는다
    number //= 10    

print(result)

"""
나의 접근방법은 나머지를 하나하나씩 더해 준다 이었다. 
나머지를 하나하나 모아서 이걸 덧붙여주면 된다고 생각했다. 
이전 문제에서 핵심은 str는 하나하나를 불러 올 수 있고, 순서화 시킬 수 있지만
int는 할 수 없었고 어쩔 수 없이 자리수를 이용하여 문제를 해결하였다. 
그래서 문제 해결을 만약 str이었다면 어떻게 했을까를 중심을 가져갔다. 
반면 쌤의 풀이는 str의 속성이 아니라 int의 특징으로 가져갔다. 
이 생각의 차이가 나의 생각을 좁게 만들었고, 결국 더 길고 복잡한 식을 만든거 같다.  
"""