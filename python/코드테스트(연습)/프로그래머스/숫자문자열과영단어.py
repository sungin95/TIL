def solution(word):
    word = word.replace('zero', '0')
    word = word.replace('one', '1')
    word = word.replace('two', '2')
    word = word.replace('three', '3')
    word = word.replace('four', '4')
    word = word.replace('five', '5')
    word = word.replace('six', '6')
    word = word.replace('seven', '7')
    word = word.replace('eight', '8')
    word = word.replace('nine', '9')
    answer = int(word)
    return answer

# 프로그래머스는 함수만 만든다!!!