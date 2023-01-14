import string
import math


def solution(n, k):
    # 소수 판별
    def primenumber(x):
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                return False
        return True

    # 소수찾기
    prime_numbers_dict = {}
    for i in range(2, 1000010):
        if prime_numbers_dict.get(i) == None:
            prime_numbers_dict[i] = 1
            i_ = i
            while i_ < 1000010:
                i_ += i
                prime_numbers_dict[i_] = 0
    # 진수 변환 함수
    tmp = string.digits + string.ascii_lowercase

    def convert(num, base):
        q, r = divmod(num, base)
        if q == 0:
            return tmp[r]
        else:
            return convert(q, base) + tmp[r]

    ##
    str_ = list(str(convert(n, k)))
    print(str_)
    # list_save에 숫자와 0을 넣기
    list_ = ""
    list_save = []
    for s in str_:
        if s == "0":
            if list_ != "":
                list_save.append(int(list_))
            list_save.append(0)
            list_ = ""
        else:
            list_ += s
    else:
        if list_ == "":
            pass
        else:
            list_save.append(int(list_))
    print(list_save)
    #
    answer = 0
    len__ = len(list_save)
    for i in range(len__):
        # 소수를 찾을려는데 시간이 너무 걸리는거 같다. 이걸 짧게 하는 방법을 모르겠다.
        if list_save[i] != 1 and list_save[i] != 0:
            if prime_numbers_dict.get(list_save[i]) == 1:
                if (
                    (0 <= i - 1 and list_save[i - 1] == 0)
                    or (i + 1 < len__ and list_save[i + 1] == 0)
                    or (i == 0)
                ):
                    answer += 1
            elif prime_numbers_dict.get(list_save[i]) == None:
                if primenumber(list_save[i]) == True:
                    if (
                        (0 <= i - 1 and list_save[i - 1] == 0)
                        or (i + 1 < len__ and list_save[i + 1] == 0)
                        or (i == 0)
                    ):
                        answer += 1

    return answer
