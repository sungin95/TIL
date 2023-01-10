import sys

sys.stdin = open("2816.txt", "r")

N = int(input())
channel = []
answer = ""
for _ in range(N):
    data = input()
    channel.append(data)

i = 0
while True:
    if channel[i] != "KBS2":
        i += 1
        answer += "1"
    else:
        channel.remove("KBS2")
        channel = ["KBS2"] + channel
        for j in range(i):
            answer += "4"
        else:
            break

i = 0
while True:
    if channel[i] != "KBS1":
        i += 1
        answer += "1"
    else:
        channel.remove("KBS1")
        channel = ["KBS1"] + channel
        for j in range(i):
            answer += "4"
        else:
            break
print(answer)
# print(channel)
