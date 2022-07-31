T = int(input())
book_dict = {} # 판매량은 어떤 제품이 팔렸는지 이름을 다 미리 입력하기 힘들고, 카운터 할 때 하나하나 확인하며 체크를 하는 것보다 
# 딕셔너리를 이용하여 바로바로 이름과 판매량을 체크해 주는 것이 편하다. 
max_ = 0 
best_seller = []
for i in range(T): # 우선 카운터를 해 준다. 
    book = input()
    if book_dict.get(book) == None:
        book_dict[book] = 1
    else:
        book_dict[book] += 1
for book in book_dict: # 이중 가장 많이 팔린 값을 알아낸다. 
    if max_ < book_dict[book]:
        max_ = book_dict[book]
for book in book_dict: # 많이 팔린 책 리스트(판매량이 같을 경우 대비)를 만들어 준다. 
    if max_ == book_dict[book]:
        best_seller.append(book)
answer = sorted(best_seller) # 답은 이중 사전순으로 가장 앞에있는 책이다. 
print(answer[0])