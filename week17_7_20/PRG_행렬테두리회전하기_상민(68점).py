'''
아이디어 ->

1. 델타값을 만듬: col의 차이만큼 (0,1) (0,-1) 이동
              : row의 차이만큼 (1,0) (-1,0) 이동

2. box 복사본 만들고 자료로 활용

3. 원래 box에서 이동 시킴
'''
import copy
dxy = [(0, 1, 0), (1, 0, 1), (0, -1, 0), (-1, 0, 1)]

def solution(rows, columns, queries):
    box = [[0] * (columns + 1) for _ in range(rows + 1)]
    temp = 1
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            box[i][j] = temp
            temp += 1
    min_nums = []
    for query in queries:
        box_copy = copy.deepcopy(box)
        sr, sc, er, ec = query
        loop_num = [ec - sc, er - sr]
        min_num = 987654321
        # print(box_copy)
        for r, c, loop in dxy:
            for _ in range(loop_num[loop]):
                nr = sr + r
                nc = sc + c
                # print(nr, nc, box[nr][nc], box_copy[sr][sc])
                box[nr][nc] = box_copy[sr][sc]
                min_num = min(min_num, box[nr][nc])
                # print('변경후',nr, nc, box[nr][nc], box_copy[sr][sc])
                sr, sc = nr, nc
        min_nums.append(min_num)
    return min_nums
