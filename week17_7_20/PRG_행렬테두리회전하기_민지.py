"""
풀긴 풀었지만 조금 더 효율적이고 예쁘게 풀고싶다..
"""
def solution(rows, columns, queries):
    matrix = [[i * columns + j + 1 for j in range(columns)] for i in range(rows)]
    answer = []
    
    for query in queries:
        sr, sc, er, ec = query[0]-1, query[1]-1, query[2]-1, query[3]-1
        cr, cc = sr, sc
        
        min_val = prev = matrix[cr][cc]
        
        # 오른쪽으로 이동
        while cc < ec:
            temp = matrix[cr][cc+1]
            matrix[cr][cc+1] = prev
            cc += 1
            prev = temp
            if prev < min_val:
                min_val = prev
        
        # 아래로 이동
        while cr < er:
            temp = matrix[cr+1][cc]
            matrix[cr+1][cc] = prev
            cr += 1
            prev = temp
            if prev < min_val:
                min_val = prev
        
        # 왼쪽으로 이동
        while cc > sc:
            temp = matrix[cr][cc-1]
            matrix[cr][cc-1] = prev
            cc -= 1
            prev = temp
            if prev < min_val:
                min_val = prev
            
        # 위로 이동
        while cr > sr:
            temp = matrix[cr-1][cc]
            matrix[cr-1][cc] = prev
            cr -= 1
            prev = temp
            if prev < min_val:
                min_val = prev
        answer.append(min_val)

    return answer