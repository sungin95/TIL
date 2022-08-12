# from pprint import pprint
import sys
sys.stdin = open("1063.txt","r")

borad = [["."] * 8 for i in range(8)]
k, s, m = input().split() # King, Stone, m
king = [8-int(k[1]),ord(k[0])-65]
stone = [8-int(s[1]),ord(s[0])-65]

command_dict = {
    "R":(0,1),
    "L":(0,-1),
    "B":(1,0),
    "T":(-1,0),
    "RT":(-1,1),
    "LT":(-1,-1),
    "RB":(1,1),
    "LB":(1,-1)    
}
for _ in range(int(m)):
    move = input()
    if 0 <=king[0]+command_dict[move][0] and king[0]+command_dict[move][0] < 8 and 0 <= king[1]+command_dict[move][1] and king[1]+command_dict[move][1] < 8:
        # 킹이 범위에 벗어나는지
        king = [king[0]+command_dict[move][0],king[1]+command_dict[move][1]]
        if king[0] == stone[0] and king[1] == stone[1]:
            if 0 <= stone[0]+command_dict[move][0] and stone[0]+command_dict[move][0] < 8 and 0 <= stone[1]+command_dict[move][1] and stone[1]+command_dict[move][1] < 8:
                # 돌이 범위에 벗어나지지
                stone = [stone[0]+command_dict[move][0],stone[1]+command_dict[move][1]]#벗어나지 않으면 돌 이동
            else: # 벗어나면 킹 위치 리턴
                king = [king[0]-command_dict[move][0],king[1]-command_dict[move][1]]

print(chr(65 + king[1])+str(8-king[0]))
print(chr(65 + stone[1])+str(8-stone[0]))
