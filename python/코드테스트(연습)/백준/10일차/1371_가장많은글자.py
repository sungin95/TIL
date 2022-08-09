import sys



sys.stdin = open("1371.txt")
s = sys.stdin.read()
text = s.replace('\n', '').replace(' ', '')
text_dict = {
    "a":0,
    "b":0,
    "c":0,
    "d":0,
    "e":0,
    "f":0,
    "g":0,
    "h":0,
    "i":0,
    "j":0,
    "k":0,
    "l":0,
    "m":0,
    "n":0,
    "o":0,
    "p":0,
    "q":0,
    "r":0,
    "s":0,
    "t":0,
    "u":0,
    "v":0,
    "w":0,
    "x":0,
    "y":0,
    "z":0
}
max_char = 0
max_list = []

for char in text:
    text_dict[char] += 1

for alp in text_dict:
    if text_dict[alp] > max_char:
        max_char = text_dict[alp]
        max_list = []
        max_list.append(alp)
    elif text_dict[alp] == max_char:
        max_list.append(alp)
for ans in max_list:
    print(ans, end="")


