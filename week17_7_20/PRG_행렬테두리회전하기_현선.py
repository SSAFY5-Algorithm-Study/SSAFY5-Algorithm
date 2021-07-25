# easy easy easy easy easy
def solution(rows, columns, queries):
    answer = []
    # arr 설정
    arr = [[0] * columns for _ in range(rows)]
    cnt = 1
    for i in range(rows):
        for j in range(columns):
            arr[i][j] = cnt
            cnt += 1
    
    for i in range(len(queries)):
        sr,sc,er,ec = queries[i]
        sr -= 1
        sc -= 1
        er -= 1
        ec -= 1
        temp1 = arr[sr][sc]
        minV = 10001
        if temp1 < minV:
            minV = temp1
        for i in range(1, ec - sc + 1):
            temp2 = arr[sr][sc+i]
            arr[sr][sc+i] = temp1
            temp1 = temp2
            if temp1 < minV:
                minV = temp1
        
        for i in range(1, er - sr + 1):
            temp2 = arr[sr+i][ec]
            arr[sr+i][ec] = temp1
            temp1 = temp2
            if temp1 < minV:
                minV = temp1
        for i in range(1, ec - sc + 1):
            temp2 = arr[er][ec-i]
            arr[er][ec-i] = temp1
            temp1 = temp2
            if temp1 < minV:
                minV = temp1
        for i in range(1, er - sr + 1):
            temp2 = arr[er-i][sc]
            arr[er-i][sc] = temp1
            temp1 = temp2
            if temp1 < minV:
                minV = temp1
        answer.append(minV)
        
    return answer