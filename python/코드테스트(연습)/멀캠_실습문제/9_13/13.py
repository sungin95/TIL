word = "apple"
n = len(word)
upside_down = ""


for char in range(n-1,-1,-1):
    upside_down += word[char]


print(upside_down)
 
 