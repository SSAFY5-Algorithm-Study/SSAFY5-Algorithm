def solution(scores):
    def change_to_score(data):
        if data >= 90:
            return 'A'
        elif data >= 80:
            return 'B'
        elif data >= 70:
            return 'C'
        elif data >= 50:
            return 'D'
        return 'F'
    
    groups = [[] for _ in range(len(scores))]
    answer = ''
    # 각자 배열생성
    for score in scores:
        for i in range(len(score)):
            groups[i].append(score[i])
    
    for i in range(len(groups)):
        current_group = groups[i]
        group_num = len(current_group)
        print(current_group, 'current')
        own_evaluation = current_group[i]
        num_count = current_group.count(own_evaluation)

        num_sum = sum(current_group)
        if num_count == 1:
            max_num = max(current_group)
            min_num = min(current_group)
            print(num_count, 'count', max_num, min_num)
            if own_evaluation == max_num or own_evaluation == min_num:
                print(own_evaluation, 'own')
                num_sum -= own_evaluation
                group_num -= 1
        final_score = num_sum / group_num
        answer += change_to_score(final_score)

    
    return answer
