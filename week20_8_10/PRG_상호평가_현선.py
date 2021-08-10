def solution(scores):
    answer = ''
    scores2 = list(zip(*scores))
    for i in range(len(scores)):
        cnt = 0
        total = 0
        for j in range(len(scores[i])):
            if j == i:
                if scores2[i][j] == max(scores2[i]) and scores2[i].count(scores2[i][j]) == 1:
                    continue
                elif scores2[i][j] == min(scores2[i]) and scores2[i].count(scores2[i][j]) == 1:
                    continue
            cnt += 1
            total += scores[j][i]
        avg = total / cnt
        if avg >= 90:
            alpha = 'A'
        elif avg >= 80:
            alpha = 'B'
        elif avg >= 70:
            alpha = 'C'
        elif avg >= 50:
            alpha = 'D'
        else:
            alpha = 'F'
        answer += alpha
    return answer