def solution(weights, head2head):
    answer = []
    dic = dict()
    for i,j in enumerate(weights):
        # 몸무게, 승률, 무거운 사람 이긴 횟수         
        dic[i+1] = [j, 0.0, 0]
    # print(dic)
    for i in range(len(head2head)):
        game_cnt = 0
        win_cnt = 0
        for j in range(len(head2head[i])):
            if head2head[i][j] == 'N':
                continue
            game_cnt += 1
            if head2head[i][j] == 'W':
                win_cnt += 1
                if weights[i] < weights[j]:
                    dic[i+1][2] += 1
        # round 써서 소수 반올림 처리하면 틀림
        dic[i+1][1] = win_cnt/game_cnt * 100 if game_cnt else 0
    # print(dic)
    # print(dic.items())
    x = sorted(dic.items(), key=lambda x:(-x[1][1], -x[1][2], -x[1][0], x[0]))
    # print(x)
                    
    for boxer_info in x:
        answer.append(boxer_info[0])
    return answer