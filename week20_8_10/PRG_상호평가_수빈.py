def solution(scores):
    answer = ''
    scores = list(zip(*scores))

    length = len(scores)
    for i in range(length):
        min_score = min(scores[i])
        max_score = max(scores[i])
        my_score = scores[i][i]
        
        if (my_score == min_score or my_score == max_score) and scores[i].count(my_score) == 1:
            average = (sum(scores[i]) - my_score) / (length - 1)
        else:
            average = sum(scores[i]) / length
            
        if average >= 90:
            answer += 'A'
        elif average >= 80:
            answer += 'B' 
        elif average >= 70:
            answer += 'C' 
        elif average >= 50:
            answer += 'D' 
        else:
            answer += 'F' 
    
    return answer