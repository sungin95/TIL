import sys

sys.stdin = open("16120.txt", "r")

from collections import deque

ppap = input()


def ppap_function(ppap):
    ppap = deque(ppap)
    i = 0
    ppap2 = deque()
    while len(ppap) >= 4:
        if (
            ppap[i] == "P"
            and ppap[i + 1] == "P"
            and ppap[i + 2] == "A"
            and ppap[i + 3] == "P"
        ):

            ppap.popleft()
            ppap.popleft()
            ppap.popleft()
            if ppap2:
                c = ppap2.pop()
                ppap.appendleft(c)

        else:
            a = ppap.popleft()
            ppap2.append(a)

    return ppap


a = len(ppap)
ppap = ppap_function(ppap)

if ppap == deque(["P"]):
    print("PPAP")
else:
    print("NP")
