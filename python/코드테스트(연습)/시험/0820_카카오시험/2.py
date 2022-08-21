def solution(orders, course):
    answer = []
    for co in course:
        order_dict = {}
        max_list = []
        max_ = 2
        for order2 in orders:
            oooo = []
            for ooo in order2:
                oooo.append(ord(ooo))
            oooo.sort()
            order = ""
            for oo in oooo:
                order += chr(oo)

            for i in range(len(order)):
                for j in range(i+1,len(order)):
                    if co == 2 and len(order) >= 2:
                        if order_dict.get(order[i] + order[j]) == None:
                            order_dict[order[i] + order[j]] = 1
                        else:
                            order_dict[order[i] + order[j]] += 1
                        if order_dict[order[i] + order[j]] > max_:
                            max_ = order_dict[order[i] + order[j]]
                            max_list = []
                            max_list.append(order[i] + order[j])
                        elif order_dict[order[i] + order[j]] == max_:
                            max_list.append(order[i] + order[j])
                            
                    else:
                        
                        for k in range(j+1,len(order)):
                            if co == 3 and len(order) >= 3:
                                if order_dict.get(order[i] + order[j]+ order[k]) == None:
                                    order_dict[order[i] + order[j] + order[k]] = 1
                                else:
                                    order_dict[order[i] + order[j] + order[k]] += 1
                                if order_dict[order[i] + order[j] + order[k]] > max_:
                                    max_ = order_dict[order[i] + order[j] + order[k]]
                                    max_list = []
                                    max_list.append(order[i] + order[j] + order[k])
                                elif order_dict[order[i] + order[j] + order[k]] == max_:
                                    max_list.append(order[i] + order[j] + order[k])

                            else:

                                for q in range(k+1,len(order)):
                                    if co == 4 and len(order) >= 4:
                                        if order_dict.get(order[i] + order[j]+ order[k] + order[q]) == None:
                                            order_dict[order[i] + order[j] + order[k] + order[q]] = 1
                                        else:
                                            order_dict[order[i] + order[j] + order[k] + order[q]] += 1
                                        if order_dict[order[i] + order[j] + order[k] + order[q]] > max_:
                                            max_ = order_dict[order[i] + order[j] + order[k] + order[q]]
                                            max_list = []
                                            max_list.append(order[i] + order[j] + order[k] + order[q])
                                        elif order_dict[order[i] + order[j] + order[k] + order[q]] == max_:
                                            max_list.append(order[i] + order[j] + order[k] + order[q])
                                    else:
                                        for w in range(q+1,len(order)):
                                            if co == 5 and len(order) >= 5:
                                                if order_dict.get(order[i] + order[j]+ order[k] + order[q] + order[w]) == None:
                                                    order_dict[order[i] + order[j] + order[k] + order[q]] = 1
                                                else:
                                                    order_dict[order[i] + order[j] + order[k] + order[q]] += 1
                                                if order_dict[order[i] + order[j] + order[k] + order[q]] > max_:
                                                    max_ = order_dict[order[i] + order[j] + order[k] + order[q]]
                                                    max_list = []
                                                    max_list.append(order[i] + order[j] + order[k] + order[q])
                                                elif order_dict[order[i] + order[j] + order[k] + order[q]] == max_:
                                                    max_list.append(order[i] + order[j] + order[k] + order[q])                            

                        
                

        for ans in max_list:
            answer.append(ans)
        answer.sort()
        print(order_dict)  
        print(max_list)
        print(answer)
        print()
    return answer