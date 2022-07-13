word = "apple"
remove = "a" # 한글자 영어 제거 가능

conversion = ""
for char in word:
    if char != remove:
        conversion += char


print(conversion)
