


# 효율성 0
def solution(info, query):
    language, work, career, food, score = [], [], [], [], []
    for i in range(len(info)):
        info[i] = info[i].split()
    answer = []
    for i in range(len(query)):
        total_cnt = 0
        query[i] = query[i].split()
        for inf in info:
            cnt = 0
            if query[i][0] == '-' or query[i][0] == inf[0]:
                cnt += 1
                if query[i][2] == '-' or query[i][2] == inf[1]:
                    cnt += 1
                    if query[i][4] == '-' or query[i][4] == inf[2]:
                        cnt += 1
                        if query[i][6] == '-' or query[i][6] == inf[3]:
                            cnt += 1
                            if int(inf[4]) >= int(query[i][7]):
                                cnt += 1
            if cnt == 5:
                total_cnt += 1
        answer.append(total_cnt)
    return answer