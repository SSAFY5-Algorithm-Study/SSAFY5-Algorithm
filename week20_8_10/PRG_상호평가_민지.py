def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 50:
        return "D"
    return "F"

def solution(scores):
    answer = ''
    # 학생 수
    N = len(scores)
    # score 배열의 x/y축을 바꾼다
    # 내가 평가한 점수가 아닌 내가 평가받은 점수들이 같이 묶이도록
    scores = list(zip(*scores))
    for i in range(N):
        min_score = min(scores[i])
        max_score = max(scores[i])
        # 1. 내가 평가한 점수가 min인 경우
        if scores[i][i] == min_score and scores[i].count(min_score) == 1:
            avg = (sum(scores[i])-min_score) / (N-1) 
        # 2. 내가 평가한 점수가 max인 경우
        elif scores[i][i] == max_score and scores[i].count(max_score) == 1:
            avg = (sum(scores[i])-max_score) / (N-1)
        # 3. 둘다 아닌 경우
        else:
            avg = sum(scores[i]) / N
        answer += get_letter_grade(avg)
    return answer