str_dict = {
    'b': 'd',
    'd': 'b',
    'q': 'p',
    'p': 'q'
}
import sys
sys.stdin = open("03.txt", "r")
t = int(input())
for test_case in range(1, t + 1):
    str_ =  input()
    revers_str = ""
    for i in str_:
        revers_str =  str_dict[i] + revers_str 
    print(f"#{test_case} {revers_str}")


