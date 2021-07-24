def move(dr, dc, prev):
    global matrix, cr, cc, min_val
    temp = matrix[cr+dr][cc+dc]
    matrix[cr+dr][cc+dc] = prev
    
    cr, cc = cr+dr, cc+dc
    if temp < min_val:
        min_val = temp
        
    return temp
    
def solution(rows, columns, queries):
    answer = []
    matrix = [[i * columns + j + 1 for j in range(columns)] for i in range(rows)]
    for query in queries:
        sr, sc, er, ec = query[0]-1, query[1]-1, query[2]-1, query[3]-1
        cr, cc = sr, sc
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        
        min_val = prev = matrix[cr][cc]
        
        # 오른쪽으로 이동
        while cc < ec:
            prev = move(dr[0], dc[0], prev)
        
        # 아래로 이동
        while cr < er:
            prev = move(dr[1], dc[1], prev)
        
        # 왼쪽으로 이동
        while cc > sc:
            prev = move(dr[2], dc[2], prev)
            
        # 위로 이동
        while cr > sr:
            prev = move(dr[3], dc[3], prev)
            
        answer.append(min_val)

    return answer

print(solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))