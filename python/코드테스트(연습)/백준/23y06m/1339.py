import sys

sys.stdin = open("1339.txt", "r")


N = int(input())
total_word = [[0, chr(i + 65)] for i in range(26)]
for i in range(N):
    word = list(input())
    for i in range(len(word)):
        total_word[ord(word[-i - 1]) - 65][0] += 10**i
total_word.sort(reverse=True)

# 정답 도출
answer = 0
for i in range(10):
    answer += total_word[i][0] * (9 - i)

print(answer)


# 정렬 순서에 맞게 알파벳에 높은 숫자 부여
# alfab_num = dict()
# for i in range(10):
#     try:
#         alfab_num[total_word[i][1]] = 9 - i
#     except:
#         break


# if max_len < len(word):
#     max_len = len(word)
# total_word = [[] for i in range(max_len)]
# for word in word_list:
#     for i in range(len(word)):
#         total_word[-i - 1].append(word[-i - 1])

# 가중치를 계산해 줍니다.(앞에 있을 수록 중요한 수니까)
# dict_alfab = dict()
# for i in range(max_len):
#     for w in total_word[-i - 1]:
#         if dict_alfab.get(w) == None:
#             dict_alfab[w] = 10**i
#         else:
#             dict_alfab[w] += 10**i


# # 딕셔너리 => 리스트 옮겨서 저장 후 정렬
# importance = []
# for w in dict_alfab:
#     importance.append((dict_alfab[w], w))
# importance.sort(reverse=True)

# # 정렬 순서에 맞게 알파벳에 높은 숫자 부여
# alfab_num = dict()
# for i in range(10):
#     try:
#         alfab_num[importance[i][1]] = 9 - i
#     except:
#         break

# # 정답 도출
# answer = 0
# for word in word_list:
#     w_num = ""
#     for w in word:
#         w_num += str(alfab_num[w])
#     answer += int(w_num)
# print(answer)
