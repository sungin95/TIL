T = int(input())
for test_case in range(1, T + 1):
    n, spell_ = input().split()
    n = int(n)
    spell_modify = ''

    for char in spell_[:n-1]:
        spell_modify += char
    
    for char in spell_[n:]:
        spell_modify += char
    print(f"{spell_modify}")