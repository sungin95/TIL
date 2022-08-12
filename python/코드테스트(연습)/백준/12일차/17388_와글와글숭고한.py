soongsil, korea, hanyang = map(int, input().split())

if soongsil + korea + hanyang >= 100:
    print("OK")
else:
    if soongsil < korea and soongsil < hanyang:
        print("Soongsil")
    elif korea < soongsil and korea < hanyang:
        print("Korea")
    elif hanyang < korea and hanyang < soongsil:
        print("Hanyang")