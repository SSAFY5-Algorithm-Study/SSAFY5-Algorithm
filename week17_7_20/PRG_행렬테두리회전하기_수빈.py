def solution(rows, columns, queries):
    answer = []
    # 초기 행렬 만들기
    arr = [[] for _ in range(rows)]
    for i in range(rows):
        for j in range(1, columns+1):
            arr[i].append((i*columns) + j)
    
    # 각 회전별 
    for q in queries:
        # 인덱스 값 맞춰주기 위한 작업
        x1, y1, x2, y2 = [x-1 for x in q]
        temp = arr[x1][y1]
        min_num = temp
        
        # 왼쪽 줄 회전
        for i in range(x1, x2):
            arr[i][y1] = arr[i+1][y1]
            min_num = min(min_num, arr[i+1][y1])
        
        # 아래 줄 회전
        for i in range(y1, y2):
            arr[x2][i] = arr[x2][i+1]
            min_num = min(min_num, arr[x2][i+1])
        
        # 오른쪽 줄 회전
        for i in range(x2, x1, -1):
            arr[i][y2] = arr[i-1][y2]
            min_num = min(min_num, arr[i-1][y2])
        
        # 윗 줄 회전
        for i in range(y2, y1, -1):
            arr[x1][i] = arr[x1][i-1]
            min_num = min(min_num, arr[x1][i-1])
            
        arr[x1][y1+1] = temp
        answer.append(min_num)

    return answer