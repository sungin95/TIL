str_ = input()
answer = ''
ban = 'CAMBRIDGE'

for char in str_:
    if char not in ban:
        answer += char
print(answer)