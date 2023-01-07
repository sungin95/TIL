# 왜 맞틀???


def solution(hp):
    ant_list = [5, 3, 1]
    min_ = [1001]
    ant_dict = {}

    def add_ant(cnt, rest_hp):
        # 가지 치기
        if ant_dict.get(rest_hp) == None:
            ant_dict[rest_hp] = cnt
        else:
            if ant_dict[rest_hp] <= cnt:
                return
            else:
                ant_dict[rest_hp] = cnt
        if cnt >= min_[0]:
            return
        # 계산
        cnt += 1
        for i in range(3):
            rest_hp__ = rest_hp - ant_list[i]
            if rest_hp__ > 0:
                add_ant(cnt, rest_hp__)
            elif rest_hp__ == 0:
                if min_[0] > cnt:
                    min_[0] = cnt
        return

    add_ant(0, hp)
    answer = min_[0]
    print(ant_dict)
    return answer
