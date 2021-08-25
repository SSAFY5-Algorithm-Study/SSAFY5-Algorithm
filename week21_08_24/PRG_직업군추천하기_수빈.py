def solution(table, languages, preference):
    table.sort()
    selected = ''
    max_score = 0
    
    for job in table:
        scores = job.split()
        score = 0
        for i in range(len(languages)):
            if languages[i] in scores:
                score += (6 - scores.index(languages[i])) * preference[i]
        
        if score > max_score:
            selected = scores[0]
            max_score = score
            
    return selected